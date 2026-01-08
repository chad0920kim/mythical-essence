"""
Mythical Essence - Face to God Matching Service
Main FastAPI Application
"""
import json
import uuid
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
import uvicorn

from app.config import (
    APP_NAME, APP_DESCRIPTION, DEBUG,
    STATIC_DIR, TEMPLATES_DIR, LOCALES_DIR, UPLOADS_DIR,
    SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE,
    MAX_IMAGE_SIZE, ALLOWED_EXTENSIONS,
    FREE_FACE_SWAP_COUNT, AD_REQUIRED_AFTER,
    ADSENSE_CLIENT_ID, ADSENSE_AD_SLOT
)
from app.services.face_analysis import get_face_analyzer
from app.services.god_matcher import match_face_to_god, get_primary_match
from app.services.face_swap import get_face_swapper, convert_to_base64
from app.models.gods import GODS_DATABASE, Culture
from app.models.descriptions_registry import (
    ALL_CHARACTER_DESCRIPTIONS,
    CharacterCategory,
    get_character_description,
    get_character_category,
    get_characters_by_category,
    get_all_categories,
    get_category_name,
    get_category_counts,
    get_total_character_count,
)


# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version="1.0.0",
    debug=DEBUG
)

# Mount static files
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Initialize templates
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# ============================================
# Localization Helper
# ============================================
def load_translations(lang: str) -> dict:
    """Load translations for a given language."""
    lang_file = LOCALES_DIR / f"{lang}.json"
    if not lang_file.exists():
        lang_file = LOCALES_DIR / f"{DEFAULT_LANGUAGE}.json"

    try:
        with open(lang_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


# Cache for character translations
_character_translations_cache: dict[str, dict] = {}


def load_character_translations(lang: str) -> dict:
    """Load character translations for a given language."""
    if lang in _character_translations_cache:
        return _character_translations_cache[lang]

    # Try to load language-specific translations
    char_file = LOCALES_DIR / "characters" / f"{lang}.json"
    if char_file.exists():
        try:
            with open(char_file, 'r', encoding='utf-8') as f:
                translations = json.load(f)
                _character_translations_cache[lang] = translations
                return translations
        except Exception:
            pass

    return {}


def get_translated_character(character, lang: str) -> dict:
    """Get character data with translations for the current language."""
    # For Korean and English, use the built-in fields
    if lang in ["ko", "en"]:
        return {
            "id": character.id,
            "name": character.name_ko if lang == "ko" else character.name_en,
            "name_alt": character.name_en if lang == "ko" else character.name_ko,
            "tagline": character.tagline_ko if lang == "ko" else character.tagline_en,
            "description": character.description_ko if lang == "ko" else character.description_en,
            "traits": character.traits_ko if lang == "ko" else character.traits_en,
            "story": character.story_ko if lang == "ko" else character.story_en,
            "match_message": character.match_message_ko if lang == "ko" else character.match_message_en,
            "aliases": character.aliases,
            "era": character.era,
            "related_characters": character.related_characters,
        }

    # For other languages, try to load translations
    translations = load_character_translations(lang)
    char_trans = translations.get(character.id, {})

    return {
        "id": character.id,
        "name": char_trans.get(f"name_{lang}", character.name_en),
        "name_alt": character.name_en,  # Always show English as alternative
        "tagline": char_trans.get(f"tagline_{lang}", character.tagline_en),
        "description": char_trans.get(f"description_{lang}", character.description_en),
        "traits": char_trans.get(f"traits_{lang}", character.traits_en),
        "story": char_trans.get(f"story_{lang}", character.story_en),
        "match_message": char_trans.get(f"match_message_{lang}", character.match_message_en),
        "aliases": character.aliases,
        "era": character.era,
        "related_characters": character.related_characters,
    }


def get_user_language(request: Request) -> str:
    """Get user's preferred language from cookie or Accept-Language header."""
    # Check cookie first
    lang = request.cookies.get("lang")
    if lang and lang in SUPPORTED_LANGUAGES:
        return lang

    # Check Accept-Language header
    accept_lang = request.headers.get("Accept-Language", "")
    for lang_code in SUPPORTED_LANGUAGES:
        if lang_code in accept_lang.lower():
            return lang_code

    return DEFAULT_LANGUAGE


# ============================================
# Template Context Helper
# ============================================
def get_usage_count(request: Request) -> int:
    """Get user's face swap usage count from cookie."""
    try:
        return int(request.cookies.get("face_swap_count", "0"))
    except (ValueError, TypeError):
        return 0


def get_ad_watched(request: Request) -> bool:
    """Check if user has watched ad for current session."""
    return request.cookies.get("ad_watched", "0") == "1"


def get_base_context(request: Request) -> dict:
    """Get base context for templates."""
    lang = get_user_language(request)
    translations = load_translations(lang)
    usage_count = get_usage_count(request)

    return {
        "request": request,
        "lang": lang,
        "t": translations,
        "languages": SUPPORTED_LANGUAGES,
        "app_name": APP_NAME,
        "usage_count": usage_count,
        "free_limit": FREE_FACE_SWAP_COUNT,
        "ad_required": usage_count >= AD_REQUIRED_AFTER,
        "adsense_client_id": ADSENSE_CLIENT_ID,
        "adsense_ad_slot": ADSENSE_AD_SLOT,
    }


# ============================================
# Routes
# ============================================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page with upload form."""
    context = get_base_context(request)
    return templates.TemplateResponse("index.html", context)


@app.get("/set-language/{lang}")
async def set_language(lang: str, request: Request):
    """Set user's preferred language."""
    if lang not in SUPPORTED_LANGUAGES:
        lang = DEFAULT_LANGUAGE

    # Redirect back to referer or home
    referer = request.headers.get("Referer", "/")
    response = RedirectResponse(url=referer, status_code=302)
    response.set_cookie(key="lang", value=lang, max_age=31536000, path="/")  # 1 year
    return response


@app.get("/api/usage-status")
async def get_usage_status(request: Request):
    """Get current usage status for face swap."""
    usage_count = get_usage_count(request)
    ad_watched = get_ad_watched(request)

    return JSONResponse(content={
        "usage_count": usage_count,
        "free_limit": FREE_FACE_SWAP_COUNT,
        "ad_required": usage_count >= AD_REQUIRED_AFTER and not ad_watched,
        "can_use": usage_count < FREE_FACE_SWAP_COUNT or ad_watched,
    })


@app.post("/api/ad-watched")
async def confirm_ad_watched(request: Request):
    """Confirm that user has watched an ad."""
    response = JSONResponse(content={"success": True, "message": "Ad confirmed"})
    # Set cookie to mark ad as watched (expires in 1 hour)
    response.set_cookie(key="ad_watched", value="1", max_age=3600, path="/")
    return response


@app.post("/analyze")
async def analyze_face(
    request: Request,
    file: UploadFile = File(...),
    region: Optional[str] = Form(None)
):
    """Analyze uploaded face and return matching god."""
    lang = get_user_language(request)
    translations = load_translations(lang)

    # Check usage limits
    usage_count = get_usage_count(request)
    ad_watched = get_ad_watched(request)

    # If exceeded free limit and haven't watched ad, require ad
    if usage_count >= FREE_FACE_SWAP_COUNT and not ad_watched:
        return JSONResponse(
            content={
                "success": False,
                "require_ad": True,
                "message": translations.get("error_ad_required", "Please watch an ad to continue"),
                "usage_count": usage_count,
            },
            status_code=402  # Payment Required
        )

    # Validate file
    if not file.filename:
        raise HTTPException(status_code=400, detail=translations.get("error_upload", "Upload error"))

    # Check file extension
    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Invalid file format. Allowed: {', '.join(ALLOWED_EXTENSIONS)}")

    # Read file
    contents = await file.read()

    # Check file size
    if len(contents) > MAX_IMAGE_SIZE:
        raise HTTPException(status_code=400, detail="File too large. Maximum size is 10MB.")

    # Analyze face
    analyzer = get_face_analyzer()
    features = analyzer.analyze_from_bytes(contents)

    if features is None:
        raise HTTPException(status_code=400, detail=translations.get("error_no_face", "No face detected"))

    # Get region from language if not specified
    if not region:
        lang_info = SUPPORTED_LANGUAGES.get(lang, {})
        region = lang_info.get("region")

    # Match to gods
    matches = match_face_to_god(features, region=region, top_n=5)

    if not matches:
        raise HTTPException(status_code=500, detail=translations.get("error_generic", "Something went wrong"))

    primary_match = matches[0]

    # Generate result image (optional - may fail without proper templates)
    result_image_base64 = None
    try:
        import numpy as np
        import cv2

        nparr = np.frombuffer(contents, np.uint8)
        source_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if source_image is not None:
            swapper = get_face_swapper()
            result_image = swapper.swap_face(source_image, primary_match.god.id)
            if result_image is not None:
                result_image_base64 = convert_to_base64(result_image)
    except Exception as e:
        print(f"Image processing error: {e}")

    # Generate unique result ID
    result_id = str(uuid.uuid4())[:8]

    # Prepare response
    response_data = {
        "success": True,
        "result_id": result_id,
        "primary_match": {
            "god_id": primary_match.god.id,
            "god_name": primary_match.god.id.replace("_", " ").title(),
            "culture": primary_match.god.culture.value,
            "archetype": primary_match.god.archetype.value,
            "element": primary_match.god.element,
            "domain": primary_match.god.domain,
            "symbol": primary_match.god.symbol,
            "color": primary_match.god.color,
            "match_score": round(primary_match.match_score * 100),
            "reasoning": primary_match.reasoning,
        },
        "other_matches": [
            {
                "god_id": m.god.id,
                "god_name": m.god.id.replace("_", " ").title(),
                "culture": m.god.culture.value,
                "match_score": round(m.match_score * 100),
            }
            for m in matches[1:]
        ],
        "face_analysis": {
            "face_shape": features.face_shape,
            "eye_type": features.eye_type,
            "symmetry": round(features.symmetry_score * 100),
            "intensity": round(features.intensity_level * 100),
        },
        "result_image": result_image_base64,
        "usage_count": usage_count + 1,
    }

    # Create response and update usage cookie
    response = JSONResponse(content=response_data)
    new_count = usage_count + 1
    response.set_cookie(key="face_swap_count", value=str(new_count), max_age=86400, path="/")  # 24 hours

    # Reset ad_watched after use (require new ad for next time)
    if ad_watched:
        response.set_cookie(key="ad_watched", value="0", max_age=0, path="/")

    return response


@app.get("/result/{result_id}", response_class=HTMLResponse)
async def result_page(request: Request, result_id: str):
    """Display result page (for sharing)."""
    context = get_base_context(request)
    context["result_id"] = result_id
    return templates.TemplateResponse("result.html", context)


@app.get("/god/{god_id}", response_class=HTMLResponse)
async def god_detail(request: Request, god_id: str, from_culture: Optional[str] = None):
    """Display god detail page."""
    god = GODS_DATABASE.get(god_id)
    if not god:
        raise HTTPException(status_code=404, detail="God not found")

    context = get_base_context(request)
    context["god"] = god
    context["from_culture"] = from_culture
    return templates.TemplateResponse("god_detail.html", context)


@app.get("/privacy", response_class=HTMLResponse)
async def privacy_policy(request: Request):
    """Display privacy policy page."""
    context = get_base_context(request)
    return templates.TemplateResponse("privacy.html", context)


@app.get("/terms", response_class=HTMLResponse)
async def terms_of_service(request: Request):
    """Display terms of service page."""
    context = get_base_context(request)
    return templates.TemplateResponse("terms.html", context)


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Display contact form page."""
    context = get_base_context(request)
    return templates.TemplateResponse("contact.html", context)


@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request, culture: Optional[str] = None):
    """Display gallery of all gods."""
    context = get_base_context(request)

    if culture:
        try:
            culture_enum = Culture(culture)
            gods = [g for g in GODS_DATABASE.values() if g.culture == culture_enum]
        except ValueError:
            gods = list(GODS_DATABASE.values())
    else:
        gods = list(GODS_DATABASE.values())

    context["gods"] = gods
    context["cultures"] = list(Culture)
    context["selected_culture"] = culture
    context["descriptions"] = ALL_CHARACTER_DESCRIPTIONS

    return templates.TemplateResponse("gallery.html", context)


# ============================================
# Character Browser Routes (with descriptions)
# ============================================
@app.get("/characters", response_class=HTMLResponse)
async def character_browser(request: Request, category: Optional[str] = None):
    """Display character browser with all characters organized by category."""
    context = get_base_context(request)
    lang = context["lang"]

    # Get categories with their display names
    categories_data = []
    for cat in get_all_categories():
        categories_data.append({
            "value": cat.value,
            "name_en": get_category_name(cat, "en"),
            "name_ko": get_category_name(cat, "ko"),
        })

    # Get characters for selected category or all
    if category:
        try:
            cat_enum = CharacterCategory(category)
            characters_raw = get_characters_by_category(cat_enum)
        except ValueError:
            characters_raw = list(ALL_CHARACTER_DESCRIPTIONS.values())
    else:
        characters_raw = list(ALL_CHARACTER_DESCRIPTIONS.values())

    # Translate characters
    characters = [get_translated_character(c, lang) for c in characters_raw]

    # Sort characters by name
    characters.sort(key=lambda c: c["name"])

    context["characters"] = characters
    context["categories"] = categories_data
    context["selected_category"] = category
    context["category_counts"] = {cat.value: count for cat, count in get_category_counts().items()}
    context["total_count"] = get_total_character_count()

    return templates.TemplateResponse("characters.html", context)


@app.get("/character/{char_id}", response_class=HTMLResponse)
async def character_detail(request: Request, char_id: str, from_category: Optional[str] = None):
    """Display detailed character information."""
    character_raw = get_character_description(char_id)
    if not character_raw:
        raise HTTPException(status_code=404, detail="Character not found")

    context = get_base_context(request)
    lang = context["lang"]

    # Translate character
    character = get_translated_character(character_raw, lang)
    context["character"] = character
    context["from_category"] = from_category

    # Get category info
    category = get_character_category(char_id)
    if category:
        context["category"] = {
            "value": category.value,
            "name_en": get_category_name(category, "en"),
            "name_ko": get_category_name(category, "ko"),
        }

    # Get related characters if any
    if character_raw.related_characters:
        related = []
        for rel_id in character_raw.related_characters[:5]:  # Limit to 5
            rel_char = get_character_description(rel_id)
            if rel_char:
                related.append(get_translated_character(rel_char, lang))
        context["related_characters"] = related

    return templates.TemplateResponse("character_detail.html", context)


@app.get("/api/characters")
async def api_characters(category: Optional[str] = None, limit: int = 50):
    """API endpoint to get characters list with descriptions."""
    if category:
        try:
            cat_enum = CharacterCategory(category)
            characters = get_characters_by_category(cat_enum)
        except ValueError:
            characters = list(ALL_CHARACTER_DESCRIPTIONS.values())
    else:
        characters = list(ALL_CHARACTER_DESCRIPTIONS.values())

    return {
        "total": len(characters),
        "characters": [
            {
                "id": c.id,
                "name_en": c.name_en,
                "name_ko": c.name_ko,
                "tagline_en": c.tagline_en,
                "tagline_ko": c.tagline_ko,
                "category": get_character_category(c.id).value if get_character_category(c.id) else None,
            }
            for c in characters[:limit]
        ]
    }


@app.get("/api/gods")
async def api_gods(culture: Optional[str] = None, limit: int = 50):
    """API endpoint to get gods list."""
    if culture:
        try:
            culture_enum = Culture(culture)
            gods = [g for g in GODS_DATABASE.values() if g.culture == culture_enum]
        except ValueError:
            gods = list(GODS_DATABASE.values())
    else:
        gods = list(GODS_DATABASE.values())

    return {
        "total": len(gods),
        "gods": [
            {
                "id": g.id,
                "name": g.id.replace("_", " ").title(),
                "culture": g.culture.value,
                "archetype": g.archetype.value,
                "domain": g.domain,
                "color": g.color,
            }
            for g in gods[:limit]
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "app": APP_NAME}


# ============================================
# Error Handlers
# ============================================
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    context = get_base_context(request)
    context["error"] = "Page not found"
    return templates.TemplateResponse("error.html", context, status_code=404)


@app.exception_handler(500)
async def server_error_handler(request: Request, exc):
    context = get_base_context(request)
    context["error"] = "Internal server error"
    return templates.TemplateResponse("error.html", context, status_code=500)


# ============================================
# Main Entry Point
# ============================================
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=DEBUG
    )
