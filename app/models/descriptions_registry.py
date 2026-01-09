"""
Unified Character Descriptions Registry
Combines all character descriptions from all cultural categories with category metadata
"""
from typing import Optional
from enum import Enum

from app.models.descriptions import CharacterDescription, DESCRIPTIONS_DATABASE, get_description
from app.models.descriptions_greek import GREEK_ADDITIONAL_DESCRIPTIONS
from app.models.descriptions_norse import NORSE_ADDITIONAL_DESCRIPTIONS
from app.models.descriptions_biblical import BIBLICAL_DESCRIPTIONS
from app.models.descriptions_egyptian import EGYPTIAN_ADDITIONAL_DESCRIPTIONS
from app.models.descriptions_hindu import HINDU_DESCRIPTIONS
from app.models.descriptions_chinese import CHINESE_DESCRIPTIONS
from app.models.descriptions_japanese import JAPANESE_DESCRIPTIONS
from app.models.descriptions_korean import KOREAN_ADDITIONAL_DESCRIPTIONS
from app.models.descriptions_world import WORLD_MYTHOLOGY_DESCRIPTIONS
# New cultural description files
from app.models.descriptions_roman import ROMAN_DESCRIPTIONS
from app.models.descriptions_arthurian import ARTHURIAN_DESCRIPTIONS
from app.models.descriptions_christian import CHRISTIAN_DESCRIPTIONS
from app.models.descriptions_buddhist import BUDDHIST_DESCRIPTIONS
from app.models.descriptions_celtic import CELTIC_DESCRIPTIONS
from app.models.descriptions_slavic import SLAVIC_DESCRIPTIONS
from app.models.descriptions_additional import ADDITIONAL_DESCRIPTIONS
from app.models.descriptions_additional2 import ADDITIONAL2_DESCRIPTIONS
from app.models.descriptions_additional3 import ADDITIONAL3_DESCRIPTIONS


class CharacterCategory(Enum):
    """Character cultural categories."""
    GREEK = "greek"
    NORSE = "norse"
    BIBLICAL = "biblical"
    EGYPTIAN = "egyptian"
    HINDU = "hindu"
    CHINESE = "chinese"
    JAPANESE = "japanese"
    KOREAN = "korean"
    WORLD = "world"
    # New categories
    ROMAN = "roman"
    ARTHURIAN = "arthurian"
    CHRISTIAN = "christian"
    BUDDHIST = "buddhist"
    CELTIC = "celtic"
    SLAVIC = "slavic"
    ISLAMIC = "islamic"
    MESOAMERICAN = "mesoamerican"
    PERSIAN = "persian"


# Category display names in Korean and English
CATEGORY_NAMES = {
    CharacterCategory.GREEK: {"en": "Greek Mythology", "ko": "그리스 신화"},
    CharacterCategory.NORSE: {"en": "Norse Mythology", "ko": "북유럽 신화"},
    CharacterCategory.BIBLICAL: {"en": "Biblical Figures", "ko": "성경 인물"},
    CharacterCategory.EGYPTIAN: {"en": "Egyptian Mythology", "ko": "이집트 신화"},
    CharacterCategory.HINDU: {"en": "Hindu Mythology", "ko": "힌두 신화"},
    CharacterCategory.CHINESE: {"en": "Chinese Mythology & History", "ko": "중국 신화 및 역사"},
    CharacterCategory.JAPANESE: {"en": "Japanese Mythology & History", "ko": "일본 신화 및 역사"},
    CharacterCategory.KOREAN: {"en": "Korean Mythology & History", "ko": "한국 신화 및 역사"},
    CharacterCategory.WORLD: {"en": "World Mythology", "ko": "세계 신화"},
    # New categories
    CharacterCategory.ROMAN: {"en": "Roman Mythology", "ko": "로마 신화"},
    CharacterCategory.ARTHURIAN: {"en": "Arthurian Legend", "ko": "아서 왕 전설"},
    CharacterCategory.CHRISTIAN: {"en": "Christian Saints", "ko": "기독교 성인"},
    CharacterCategory.BUDDHIST: {"en": "Buddhist Figures", "ko": "불교 인물"},
    CharacterCategory.CELTIC: {"en": "Celtic Mythology", "ko": "켈트 신화"},
    CharacterCategory.SLAVIC: {"en": "Slavic Mythology", "ko": "슬라브 신화"},
    CharacterCategory.ISLAMIC: {"en": "Islamic Heritage", "ko": "이슬람 유산"},
    CharacterCategory.MESOAMERICAN: {"en": "Mesoamerican Mythology", "ko": "메소아메리카 신화"},
    CharacterCategory.PERSIAN: {"en": "Persian Mythology", "ko": "페르시아 신화"},
}


# Mapping of character IDs to their categories
_CHARACTER_CATEGORIES: dict[str, CharacterCategory] = {}


def _register_category(char_dict: dict, category: CharacterCategory):
    """Helper to register characters to a category."""
    for char_id in char_dict.keys():
        _CHARACTER_CATEGORIES[char_id] = category


# Greek characters from base file
_GREEK_BASE_IDS = [
    "zeus", "hera", "athena", "apollo", "artemis", "ares",
    "aphrodite", "poseidon", "hades", "hermes", "dionysus", "persephone"
]
for char_id in _GREEK_BASE_IDS:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.GREEK
_register_category(GREEK_ADDITIONAL_DESCRIPTIONS, CharacterCategory.GREEK)

# Norse characters from base file
_NORSE_BASE_IDS = [
    "odin", "thor", "freya", "loki", "frigg", "baldur",
    "tyr", "hel", "heimdall", "skadi", "freyr", "njord"
]
for char_id in _NORSE_BASE_IDS:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.NORSE
_register_category(NORSE_ADDITIONAL_DESCRIPTIONS, CharacterCategory.NORSE)

# Korean characters from base file
_KOREAN_BASE_IDS = ["admiral_yi", "sejong_the_great", "gumiho"]
for char_id in _KOREAN_BASE_IDS:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.KOREAN
_register_category(KOREAN_ADDITIONAL_DESCRIPTIONS, CharacterCategory.KOREAN)

# Chinese characters from base file
_CHINESE_BASE_IDS = ["confucius", "guan_yu"]
for char_id in _CHINESE_BASE_IDS:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.CHINESE
_register_category(CHINESE_DESCRIPTIONS, CharacterCategory.CHINESE)

# Egyptian characters from base file
_EGYPTIAN_BASE_IDS = [
    "ra", "isis", "osiris", "anubis", "horus",
    "bastet", "sekhmet", "thoth", "set"
]
for char_id in _EGYPTIAN_BASE_IDS:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.EGYPTIAN
_register_category(EGYPTIAN_ADDITIONAL_DESCRIPTIONS, CharacterCategory.EGYPTIAN)

# Register additional category files
_register_category(BIBLICAL_DESCRIPTIONS, CharacterCategory.BIBLICAL)
_register_category(HINDU_DESCRIPTIONS, CharacterCategory.HINDU)
_register_category(JAPANESE_DESCRIPTIONS, CharacterCategory.JAPANESE)
_register_category(WORLD_MYTHOLOGY_DESCRIPTIONS, CharacterCategory.WORLD)

# Register new category files
_register_category(ROMAN_DESCRIPTIONS, CharacterCategory.ROMAN)
_register_category(ARTHURIAN_DESCRIPTIONS, CharacterCategory.ARTHURIAN)
_register_category(CHRISTIAN_DESCRIPTIONS, CharacterCategory.CHRISTIAN)
_register_category(BUDDHIST_DESCRIPTIONS, CharacterCategory.BUDDHIST)
_register_category(CELTIC_DESCRIPTIONS, CharacterCategory.CELTIC)
_register_category(SLAVIC_DESCRIPTIONS, CharacterCategory.SLAVIC)

# Register additional descriptions (various cultures)
# African
for char_id in ["ogun", "oshun", "yemoja"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.WORLD
# Greek Historical
for char_id in ["socrates", "plato", "aristotle", "alexander_the_great", "leonidas", "pythagoras", "hippocrates"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.GREEK
# Korean Additional
for char_id in ["hwanung", "mago", "samsin", "jacheongbi", "cheoyong", "dokkaebi", "seon_deok"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.KOREAN
# Islamic/Arabic
for char_id in ["prophet_muhammad", "ali_ibn_abi_talib", "rumi", "saladin", "avicenna", "jinn"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.ISLAMIC
# Mesoamerican
for char_id in ["huitzilopochtli", "tezcatlipoca", "coatlicue", "kukulkan", "ixchel", "chaac", "hun_hunahpu"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.MESOAMERICAN
# Mesopotamian
for char_id in ["marduk", "ishtar", "enlil"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.WORLD
# Persian
for char_id in ["mithra", "anahita", "rostam", "cyrus_the_great"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.PERSIAN
# Chinese Additional
for char_id in ["liu_bei", "mulan", "white_snake", "xu_xian", "mencius", "zhuxi"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.CHINESE
# Taoist
for char_id in ["zhuangzi", "zhang_daoling", "eight_immortals_lu"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.CHINESE
# Southeast Asian
for char_id in ["barong", "rangda", "dewi_sri", "naga", "thao_maha_phrom", "son_tinh", "thuy_tinh"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.WORLD
# Japanese Additional
for char_id in ["abe_no_seimei", "tomoe_gozen"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.JAPANESE
# Native American
for char_id in ["spider_grandmother", "thunderbird"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.WORLD
# Polynesian
for char_id in ["hina", "tangaroa"]:
    _CHARACTER_CATEGORIES[char_id] = CharacterCategory.WORLD


# Unified database combining all sources
ALL_CHARACTER_DESCRIPTIONS: dict[str, CharacterDescription] = {
    **DESCRIPTIONS_DATABASE,
    **GREEK_ADDITIONAL_DESCRIPTIONS,
    **NORSE_ADDITIONAL_DESCRIPTIONS,
    **BIBLICAL_DESCRIPTIONS,
    **EGYPTIAN_ADDITIONAL_DESCRIPTIONS,
    **HINDU_DESCRIPTIONS,
    **CHINESE_DESCRIPTIONS,
    **JAPANESE_DESCRIPTIONS,
    **KOREAN_ADDITIONAL_DESCRIPTIONS,
    **WORLD_MYTHOLOGY_DESCRIPTIONS,
    # New cultural description files
    **ROMAN_DESCRIPTIONS,
    **ARTHURIAN_DESCRIPTIONS,
    **CHRISTIAN_DESCRIPTIONS,
    **BUDDHIST_DESCRIPTIONS,
    **CELTIC_DESCRIPTIONS,
    **SLAVIC_DESCRIPTIONS,
    **ADDITIONAL_DESCRIPTIONS,
    **ADDITIONAL2_DESCRIPTIONS,
    **ADDITIONAL3_DESCRIPTIONS,
}


def get_character_description(char_id: str) -> Optional[CharacterDescription]:
    """Get character description by ID."""
    return ALL_CHARACTER_DESCRIPTIONS.get(char_id)


def get_character_category(char_id: str) -> Optional[CharacterCategory]:
    """Get the category for a character."""
    return _CHARACTER_CATEGORIES.get(char_id)


def get_characters_by_category(category: CharacterCategory) -> list[CharacterDescription]:
    """Get all characters in a category."""
    return [
        char for char_id, char in ALL_CHARACTER_DESCRIPTIONS.items()
        if _CHARACTER_CATEGORIES.get(char_id) == category
    ]


def get_all_categories() -> list[CharacterCategory]:
    """Get all available categories."""
    return list(CharacterCategory)


def get_category_name(category: CharacterCategory, lang: str = "en") -> str:
    """Get display name for a category."""
    names = CATEGORY_NAMES.get(category, {"en": category.value, "ko": category.value})
    return names.get(lang, names.get("en", category.value))


def get_category_counts() -> dict[CharacterCategory, int]:
    """Get count of characters in each category."""
    counts = {cat: 0 for cat in CharacterCategory}
    for char_id in ALL_CHARACTER_DESCRIPTIONS.keys():
        cat = _CHARACTER_CATEGORIES.get(char_id)
        if cat:
            counts[cat] += 1
    return counts


def get_total_character_count() -> int:
    """Get total number of characters."""
    return len(ALL_CHARACTER_DESCRIPTIONS)
