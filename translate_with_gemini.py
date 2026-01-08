"""
Character Translation Script using Google Gemini API
Translates character descriptions in batches
"""
import json
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")
import google.generativeai as genai

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Languages to translate to (excluding en and ko which already exist)
LANGUAGES = {
    "zh": "Simplified Chinese",
    "ja": "Japanese",
    "hi": "Hindi",
    "ar": "Arabic",
    "de": "German",
    "fr": "French",
    "es": "Spanish",
    "pt": "Portuguese",
    "ru": "Russian",
    "th": "Thai",
    "vi": "Vietnamese",
    "id": "Indonesian",
    "tr": "Turkish",
}

BATCH_SIZE = 5  # Characters per API call

def load_base_data():
    """Load base character data."""
    with open("app/locales/characters/base.json", "r", encoding="utf-8") as f:
        return json.load(f)

def translate_batch_characters(model, batch: dict, target_lang: str, lang_name: str) -> dict:
    """Translate a batch of characters using Gemini."""
    # Prepare data for translation
    to_translate = {}
    for char_id, char_data in batch.items():
        to_translate[char_id] = {
            "name": char_data["name_en"],
            "tagline": char_data["tagline_en"],
            "description": char_data["description_en"],
            "story": char_data["story_en"],
            "match_message": char_data["match_message_en"],
            "traits": char_data["traits_en"],
        }

    prompt = f"""Translate ALL the following mythological character data to {lang_name}.
Return the exact same JSON structure with translated values.
Keep proper nouns (names of gods, mythological places) in their commonly recognized form in {lang_name}.
For mythological terms, use standard translations used in that language/culture.

Characters to translate:
{json.dumps(to_translate, ensure_ascii=False, indent=2)}

Return ONLY the JSON object with the same structure, translated to {lang_name}. No markdown, no code blocks, just pure JSON."""

    response = model.generate_content(prompt)
    response_text = response.text.strip()

    # Clean up response
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    if response_text.startswith("```"):
        response_text = response_text[3:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]

    translated = json.loads(response_text.strip())

    # Format output
    result = {}
    for char_id, trans in translated.items():
        result[char_id] = {
            f"name_{target_lang}": trans.get("name", batch[char_id]["name_en"]),
            f"tagline_{target_lang}": trans.get("tagline", batch[char_id]["tagline_en"]),
            f"description_{target_lang}": trans.get("description", batch[char_id]["description_en"]),
            f"story_{target_lang}": trans.get("story", batch[char_id]["story_en"]),
            f"match_message_{target_lang}": trans.get("match_message", batch[char_id]["match_message_en"]),
            f"traits_{target_lang}": trans.get("traits", batch[char_id]["traits_en"]),
        }
    return result

def translate_language(lang_code: str, lang_name: str, resume_from: int = 0):
    """Translate all characters to a single language."""
    model = genai.GenerativeModel('gemini-2.0-flash')
    characters = load_base_data()
    char_ids = list(characters.keys())

    output_file = Path(f"app/locales/characters/{lang_code}.json")

    # Load existing translations if resuming
    if output_file.exists() and resume_from > 0:
        with open(output_file, "r", encoding="utf-8") as f:
            translations = json.load(f)
    else:
        translations = {}

    total_batches = (len(char_ids) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"\nTranslating to {lang_name} ({lang_code})...")
    print(f"Total: {len(char_ids)} characters in {total_batches} batches")

    for batch_idx in range(resume_from, total_batches):
        start_idx = batch_idx * BATCH_SIZE
        end_idx = min(start_idx + BATCH_SIZE, len(char_ids))
        batch_ids = char_ids[start_idx:end_idx]
        batch = {cid: characters[cid] for cid in batch_ids}

        print(f"  Batch {batch_idx + 1}/{total_batches}: {batch_ids}")

        try:
            batch_translations = translate_batch_characters(model, batch, lang_code, lang_name)
            translations.update(batch_translations)

            # Save after each batch
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(translations, f, ensure_ascii=False, indent=2)

            time.sleep(1)  # Rate limiting
        except Exception as e:
            print(f"    Error: {e}")
            print(f"    Resume from batch {batch_idx} with: python translate_with_gemini.py {lang_code} {batch_idx}")
            # Save what we have
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(translations, f, ensure_ascii=False, indent=2)
            raise

    print(f"Completed {lang_code}! Saved to {output_file}")

def main():
    import sys

    if len(sys.argv) >= 2:
        # Translate specific language
        lang_code = sys.argv[1]
        resume_from = int(sys.argv[2]) if len(sys.argv) >= 3 else 0

        if lang_code == "all":
            # Translate all languages
            for lc, ln in LANGUAGES.items():
                output_file = Path(f"app/locales/characters/{lc}.json")
                if output_file.exists():
                    print(f"Skipping {lc} - already exists")
                    continue
                translate_language(lc, ln)
        elif lang_code in LANGUAGES:
            translate_language(lang_code, LANGUAGES[lang_code], resume_from)
        else:
            print(f"Unknown language: {lang_code}")
            print(f"Available: {list(LANGUAGES.keys())} or 'all'")
    else:
        print("Usage: python translate_with_gemini.py <lang_code|all> [resume_from_batch]")
        print(f"Available languages: {list(LANGUAGES.keys())}")

if __name__ == "__main__":
    main()
