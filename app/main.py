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
    ADSENSE_CLIENT_ID, ADSENSE_AD_SLOT,
    GA_MEASUREMENT_ID
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
        "ga_measurement_id": GA_MEASUREMENT_ID,
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
    """Analyze uploaded face and return top 3 matching characters (without face swap)."""
    import traceback

    lang = get_user_language(request)
    translations = load_translations(lang)

    try:
        # Validate file
        if not file.filename:
            return JSONResponse(
                content={"success": False, "detail": translations.get("error_upload", "Upload error")},
                status_code=400
            )

        # Check file extension
        ext = file.filename.rsplit(".", 1)[-1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            return JSONResponse(
                content={"success": False, "detail": f"Invalid file format. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"},
                status_code=400
            )

        # Read file
        contents = await file.read()

        # Check file size
        if len(contents) > MAX_IMAGE_SIZE:
            return JSONResponse(
                content={"success": False, "detail": "File too large. Maximum size is 10MB."},
                status_code=400
            )

        # Analyze face
        print(f"Analyzing image: {len(contents)} bytes")
        analyzer = get_face_analyzer()
        features = analyzer.analyze_from_bytes(contents)

        if features is None:
            return JSONResponse(
                content={"success": False, "detail": translations.get("error_no_face", "No face detected")},
                status_code=400
            )

        print(f"Face analyzed: shape={features.face_shape}, eye={features.eye_type}")

        # Get region from language if not specified
        if not region:
            lang_info = SUPPORTED_LANGUAGES.get(lang, {})
            region = lang_info.get("region")

        # Match to gods - get top 3
        matches = match_face_to_god(features, region=region, top_n=3)

        if not matches:
            return JSONResponse(
                content={"success": False, "detail": translations.get("error_generic", "Something went wrong")},
                status_code=500
            )

        # Generate unique result ID for session tracking
        result_id = str(uuid.uuid4())[:8]

        # Store uploaded image temporarily for face swap later
        temp_image_path = UPLOADS_DIR / f"{result_id}.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(contents)

        # Helper function to get character image URL
        def get_character_image_url(god_id: str) -> str:
            for ext in ['.png', '.jpg', '.jpeg', '.webp']:
                img_path = STATIC_DIR / "images" / "gods" / f"{god_id}{ext}"
                if img_path.exists():
                    return f"/static/images/gods/{god_id}{ext}"
            return ""

        # Load character translations for current language
        char_translations = load_character_translations("base")  # base.json has all languages

        # Helper function to get translated character name
        def get_character_name(god_id: str, default_name: str) -> str:
            char_data = char_translations.get(god_id, {})
            if lang == "ko":
                return char_data.get("name_ko", default_name)
            elif lang == "en":
                return char_data.get("name_en", default_name)
            else:
                # For other languages, try language-specific file
                other_trans = load_character_translations(lang)
                other_char = other_trans.get(god_id, {})
                return other_char.get(f"name_{lang}", char_data.get("name_en", default_name))

        # Helper function to get translated match message/reasoning
        def get_match_reasoning(god_id: str, default_reasoning: str) -> str:
            char_data = char_translations.get(god_id, {})
            if lang == "ko":
                return char_data.get("match_message_ko", default_reasoning)
            elif lang == "en":
                return char_data.get("match_message_en", default_reasoning)
            else:
                other_trans = load_character_translations(lang)
                other_char = other_trans.get(god_id, {})
                return other_char.get(f"match_message_{lang}", char_data.get("match_message_en", default_reasoning))

        # Prepare top 3 matches
        top_matches = []
        for m in matches:
            default_name = m.god.id.replace("_", " ").title()
            top_matches.append({
                "god_id": m.god.id,
                "god_name": get_character_name(m.god.id, default_name),
                "culture": m.god.culture.value,
                "archetype": m.god.archetype.value,
                "element": m.god.element,
                "domain": m.god.domain,
                "symbol": m.god.symbol,
                "color": m.god.color,
                "match_score": round(m.match_score * 100),
                "reasoning": get_match_reasoning(m.god.id, m.reasoning),
                "character_image_url": get_character_image_url(m.god.id),
            })

        print(f"Top matches: {[m['god_id'] for m in top_matches]}")

        # Prepare response
        response_data = {
            "success": True,
            "result_id": result_id,
            "matches": top_matches,
            "face_analysis": {
                "face_shape": features.face_shape,
                "eye_type": features.eye_type,
                "symmetry": round(features.symmetry_score * 100),
                "intensity": round(features.intensity_level * 100),
            },
        }

        return JSONResponse(content=response_data)

    except Exception as e:
        error_msg = str(e)
        print(f"Analyze error: {error_msg}")
        traceback.print_exc()
        return JSONResponse(
            content={"success": False, "detail": translations.get("error_generic", "Something went wrong")},
            status_code=500
        )


@app.post("/api/swap-face")
async def swap_face_endpoint(
    request: Request,
    result_id: str = Form(...),
    god_id: str = Form(...)
):
    """Perform face swap for selected character (requires ad watched)."""
    import traceback

    lang = get_user_language(request)
    translations = load_translations(lang)

    try:
        # Check if ad was watched
        ad_watched = get_ad_watched(request)
        usage_count = get_usage_count(request)

        if not ad_watched and usage_count >= FREE_FACE_SWAP_COUNT:
            return JSONResponse(
                content={
                    "success": False,
                    "require_ad": True,
                    "message": translations.get("error_ad_required", "Please watch an ad to continue"),
                },
                status_code=402
            )

        # Find the temporarily stored image
        temp_image_path = UPLOADS_DIR / f"{result_id}.jpg"
        if not temp_image_path.exists():
            return JSONResponse(
                content={"success": False, "detail": translations.get("error_session_expired", "Session expired. Please upload again.")},
                status_code=400
            )

        # Read the stored image
        with open(temp_image_path, "rb") as f:
            contents = f.read()

        # Perform face swap
        import numpy as np
        import cv2

        nparr = np.frombuffer(contents, np.uint8)
        source_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        result_image_base64 = None
        character_image_url = None

        if source_image is not None:
            swapper = get_face_swapper()
            result_image = swapper.swap_face(source_image, god_id)
            if result_image is not None:
                result_image_base64 = convert_to_base64(result_image)
                print(f"Face swap successful for {god_id}")

        # Get character image URL as fallback
        for ext in ['.png', '.jpg', '.jpeg', '.webp']:
            img_path = STATIC_DIR / "images" / "gods" / f"{god_id}{ext}"
            if img_path.exists():
                character_image_url = f"/static/images/gods/{god_id}{ext}"
                break

        # Clean up temporary file
        try:
            temp_image_path.unlink()
        except Exception:
            pass

        # Prepare response
        response_data = {
            "success": True,
            "god_id": god_id,
            "result_image": result_image_base64,
            "character_image_url": character_image_url,
        }

        # Create response and update usage cookie
        response = JSONResponse(content=response_data)
        new_count = usage_count + 1
        response.set_cookie(key="face_swap_count", value=str(new_count), max_age=86400, path="/")

        # Reset ad_watched after use
        if ad_watched:
            response.set_cookie(key="ad_watched", value="0", max_age=0, path="/")

        return response

    except Exception as e:
        error_msg = str(e)
        print(f"Face swap error: {error_msg}")
        traceback.print_exc()
        return JSONResponse(
            content={"success": False, "detail": translations.get("error_generic", "Something went wrong")},
            status_code=500
        )


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


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """Display about page."""
    context = get_base_context(request)
    return templates.TemplateResponse("about.html", context)


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

    context = get_base_context(request)
    lang = context["lang"]

    if character_raw:
        # Full character description available
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
    else:
        # Fallback: Try to get basic info from GODS_DATABASE
        god = GODS_DATABASE.get(char_id)
        if not god:
            raise HTTPException(status_code=404, detail="Character not found")

        # Create minimal character info from god data
        god_name = char_id.replace("_", " ").title()

        # Get character image URL
        char_image_url = ""
        for ext in ['.png', '.jpg', '.jpeg', '.webp']:
            img_path = STATIC_DIR / "images" / "gods" / f"{char_id}{ext}"
            if img_path.exists():
                char_image_url = f"/static/images/gods/{char_id}{ext}"
                break

        context["character"] = {
            "id": char_id,
            "name": god_name,
            "tagline": f"{god.domain}",
            "image_url": char_image_url,
            "culture": god.culture.value,
            "archetype": god.archetype.value,
            "element": god.element,
            "domain": god.domain,
            "symbol": god.symbol,
            "color": god.color,
            "description": f"A {god.archetype.value} figure from {god.culture.value} mythology, associated with {god.domain}.",
            "story": "",
            "powers": [],
            "personality": [],
        }
        context["from_category"] = from_category
        context["is_basic_info"] = True  # Flag to show limited info message

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


@app.get("/sitemap.xml")
async def sitemap(request: Request):
    """Generate dynamic sitemap.xml for SEO."""
    from fastapi.responses import Response

    base_url = str(request.base_url).rstrip('/')

    # Start XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Static pages
    static_pages = ['/', '/about', '/characters', '/gallery', '/privacy', '/terms', '/contact']
    for page in static_pages:
        xml_content += f'  <url>\n    <loc>{base_url}{page}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>{"1.0" if page == "/" else "0.8"}</priority>\n  </url>\n'

    # Character detail pages
    for char_id in ALL_CHARACTER_DESCRIPTIONS.keys():
        xml_content += f'  <url>\n    <loc>{base_url}/character/{char_id}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n'

    # God detail pages
    for god_id in GODS_DATABASE.keys():
        xml_content += f'  <url>\n    <loc>{base_url}/god/{god_id}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n'

    xml_content += '</urlset>'

    return Response(content=xml_content, media_type="application/xml")


@app.get("/robots.txt")
async def robots(request: Request):
    """Serve robots.txt."""
    from fastapi.responses import Response

    base_url = str(request.base_url).rstrip('/')

    content = f"""# MythFace Robots.txt
User-agent: *
Allow: /

# Sitemaps
Sitemap: {base_url}/sitemap.xml

# Crawl-delay for polite crawling
Crawl-delay: 1
"""
    return Response(content=content, media_type="text/plain")


# ============================================
# Error Handlers
# ============================================
def is_api_request(request: Request) -> bool:
    """Check if request expects JSON response."""
    accept = request.headers.get("accept", "")
    content_type = request.headers.get("content-type", "")
    path = request.url.path

    # API endpoints or JSON accept header
    return (
        path.startswith("/api/") or
        path == "/analyze" or
        "application/json" in accept or
        "multipart/form-data" in content_type
    )


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    if is_api_request(request):
        return JSONResponse(
            content={"success": False, "detail": "Not found"},
            status_code=404
        )
    context = get_base_context(request)
    context["error"] = "Page not found"
    return templates.TemplateResponse("error.html", context, status_code=404)


@app.exception_handler(500)
async def server_error_handler(request: Request, exc):
    import traceback
    error_detail = str(exc) if exc else "Unknown error"
    print(f"500 Error on {request.url.path}: {error_detail}")
    traceback.print_exc()

    if is_api_request(request):
        return JSONResponse(
            content={"success": False, "detail": error_detail},
            status_code=500
        )
    context = get_base_context(request)
    context["error"] = "Internal server error"
    return templates.TemplateResponse("error.html", context, status_code=500)


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    import traceback
    error_detail = str(exc)
    print(f"Unhandled Exception on {request.url.path}: {error_detail}")
    traceback.print_exc()

    if is_api_request(request):
        return JSONResponse(
            content={"success": False, "detail": error_detail},
            status_code=500
        )
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
