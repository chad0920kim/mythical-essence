"""Application configuration settings."""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"
TEMPLATES_DIR = APP_DIR / "templates"
LOCALES_DIR = APP_DIR / "locales"
UPLOADS_DIR = STATIC_DIR / "uploads"
GODS_IMAGES_DIR = STATIC_DIR / "images" / "gods"

# Create directories if they don't exist
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)

# App settings
APP_NAME = "Mythical Essence"
APP_DESCRIPTION = "Discover your mythological divine counterpart"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")

# Supported languages with their cultures/regions
SUPPORTED_LANGUAGES = {
    "ko": {"name": "한국어", "region": "korea", "dir": "ltr"},
    "en": {"name": "English", "region": "western", "dir": "ltr"},
    "zh": {"name": "中文", "region": "china", "dir": "ltr"},
    "ja": {"name": "日本語", "region": "japan", "dir": "ltr"},
    "hi": {"name": "हिन्दी", "region": "india", "dir": "ltr"},
    "ar": {"name": "العربية", "region": "middle_east", "dir": "rtl"},
    "de": {"name": "Deutsch", "region": "western", "dir": "ltr"},
    "fr": {"name": "Français", "region": "western", "dir": "ltr"},
    "es": {"name": "Español", "region": "western", "dir": "ltr"},
    "pt": {"name": "Português", "region": "western", "dir": "ltr"},
    "ru": {"name": "Русский", "region": "slavic", "dir": "ltr"},
    "th": {"name": "ไทย", "region": "southeast_asia", "dir": "ltr"},
    "vi": {"name": "Tiếng Việt", "region": "southeast_asia", "dir": "ltr"},
    "id": {"name": "Bahasa Indonesia", "region": "southeast_asia", "dir": "ltr"},
    "tr": {"name": "Türkçe", "region": "middle_east", "dir": "ltr"},
}

DEFAULT_LANGUAGE = "en"

# Image processing settings
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
OUTPUT_IMAGE_SIZE = (512, 512)

# Face analysis settings
MIN_FACE_SIZE = 50  # Minimum face size in pixels
MAX_FACES = 1  # Only process one face per image
