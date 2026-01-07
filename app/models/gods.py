"""
Mythological Gods Database
Contains gods from various cultures matching supported languages
"""
from dataclasses import dataclass
from typing import Optional
from enum import Enum


class Culture(Enum):
    """Cultural origins for gods."""
    GREEK = "greek"
    ROMAN = "roman"
    NORSE = "norse"
    EGYPTIAN = "egyptian"
    HINDU = "hindu"
    CHINESE = "chinese"
    JAPANESE = "japanese"
    KOREAN = "korean"
    CELTIC = "celtic"
    SLAVIC = "slavic"
    MESOPOTAMIAN = "mesopotamian"
    ARABIC = "arabic"
    AZTEC = "aztec"
    THAI = "thai"
    VIETNAMESE = "vietnamese"
    INDONESIAN = "indonesian"
    # Additional cultures for sages, saints, and historical figures
    CHRISTIAN = "christian"
    BUDDHIST = "buddhist"
    ISLAMIC = "islamic"
    CONFUCIAN = "confucian"
    TAOIST = "taoist"
    PERSIAN = "persian"
    AFRICAN = "african"
    POLYNESIAN = "polynesian"
    NATIVE_AMERICAN = "native_american"
    MAYAN = "mayan"
    ARTHURIAN = "arthurian"


class FaceShape(Enum):
    """Face shape classifications."""
    OVAL = "oval"
    ROUND = "round"
    SQUARE = "square"
    HEART = "heart"
    OBLONG = "oblong"
    DIAMOND = "diamond"


class EyeType(Enum):
    """Eye characteristic classifications."""
    SHARP = "sharp"
    SOFT = "soft"
    WIDE = "wide"
    NARROW = "narrow"
    DEEP = "deep"
    BRIGHT = "bright"


class Archetype(Enum):
    """Jungian archetypes for personality matching."""
    RULER = "ruler"
    CREATOR = "creator"
    SAGE = "sage"
    INNOCENT = "innocent"
    EXPLORER = "explorer"
    REBEL = "rebel"
    HERO = "hero"
    WIZARD = "wizard"
    JESTER = "jester"
    EVERYMAN = "everyman"
    LOVER = "lover"
    CAREGIVER = "caregiver"


@dataclass
class God:
    """God/Deity data model."""
    id: str
    culture: Culture
    archetype: Archetype

    # Facial feature preferences for matching
    preferred_face_shapes: list[FaceShape]
    preferred_eye_types: list[EyeType]
    symmetry_preference: float  # 0.0 to 1.0
    intensity_level: float  # 0.0 to 1.0 (soft to intense features)

    # Display properties
    gender: str  # "male", "female", "neutral"
    element: str  # fire, water, earth, air, etc.
    domain: str  # What they rule over
    symbol: str  # Main symbol
    color: str  # Primary color association

    # Image template
    image_file: Optional[str] = None


# Comprehensive Gods Database
GODS_DATABASE: dict[str, God] = {
    # ============================================
    # GREEK MYTHOLOGY (그리스 신화)
    # ============================================
    "zeus": God(
        id="zeus",
        culture=Culture.GREEK,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.9,
        gender="male",
        element="sky",
        domain="King of Gods, Sky, Thunder",
        symbol="Lightning Bolt",
        color="#FFD700",
        image_file="zeus.png"
    ),
    "hera": God(
        id="hera",
        culture=Culture.GREEK,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.95,
        intensity_level=0.8,
        gender="female",
        element="air",
        domain="Queen of Gods, Marriage, Family",
        symbol="Peacock, Crown",
        color="#800080",
        image_file="hera.png"
    ),
    "athena": God(
        id="athena",
        culture=Culture.GREEK,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.95,
        intensity_level=0.7,
        gender="female",
        element="air",
        domain="Wisdom, Strategy, Crafts",
        symbol="Owl, Olive Tree",
        color="#708090",
        image_file="athena.png"
    ),
    "apollo": God(
        id="apollo",
        culture=Culture.GREEK,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="male",
        element="fire",
        domain="Sun, Music, Poetry, Healing",
        symbol="Lyre, Sun",
        color="#FFD700",
        image_file="apollo.png"
    ),
    "artemis": God(
        id="artemis",
        culture=Culture.GREEK,
        archetype=Archetype.EXPLORER,
        preferred_face_shapes=[FaceShape.HEART, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.75,
        gender="female",
        element="earth",
        domain="Hunt, Moon, Wilderness",
        symbol="Bow and Arrow, Moon",
        color="#C0C0C0",
        image_file="artemis.png"
    ),
    "ares": God(
        id="ares",
        culture=Culture.GREEK,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.7,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="War, Violence, Courage",
        symbol="Spear, Helmet",
        color="#8B0000",
        image_file="ares.png"
    ),
    "aphrodite": God(
        id="aphrodite",
        culture=Culture.GREEK,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.98,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Love, Beauty, Desire",
        symbol="Dove, Rose, Seashell",
        color="#FFB6C1",
        image_file="aphrodite.png"
    ),
    "poseidon": God(
        id="poseidon",
        culture=Culture.GREEK,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.WIDE],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="male",
        element="water",
        domain="Sea, Earthquakes, Horses",
        symbol="Trident",
        color="#1E90FF",
        image_file="poseidon.png"
    ),
    "hades": God(
        id="hades",
        culture=Culture.GREEK,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.DEEP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="earth",
        domain="Underworld, Death, Riches",
        symbol="Helm of Darkness, Cerberus",
        color="#2F4F4F",
        image_file="hades.png"
    ),
    "hermes": God(
        id="hermes",
        culture=Culture.GREEK,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.75,
        intensity_level=0.6,
        gender="male",
        element="air",
        domain="Messengers, Commerce, Thieves",
        symbol="Caduceus, Winged Sandals",
        color="#DAA520",
        image_file="hermes.png"
    ),
    "dionysus": God(
        id="dionysus",
        culture=Culture.GREEK,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.7,
        intensity_level=0.65,
        gender="male",
        element="earth",
        domain="Wine, Festivity, Madness",
        symbol="Grapevine, Thyrsus",
        color="#722F37",
        image_file="dionysus.png"
    ),
    "persephone": God(
        id="persephone",
        culture=Culture.GREEK,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.HEART, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="female",
        element="earth",
        domain="Spring, Underworld Queen",
        symbol="Pomegranate, Flowers",
        color="#9370DB",
        image_file="persephone.png"
    ),

    # ============================================
    # NORSE MYTHOLOGY (북유럽 신화)
    # ============================================
    "odin": God(
        id="odin",
        culture=Culture.NORSE,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.75,
        intensity_level=0.95,
        gender="male",
        element="air",
        domain="Wisdom, War, Death, Poetry",
        symbol="Ravens, Spear Gungnir",
        color="#4B0082",
        image_file="odin.png"
    ),
    "thor": God(
        id="thor",
        culture=Culture.NORSE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.WIDE, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="sky",
        domain="Thunder, Lightning, Storms",
        symbol="Mjolnir Hammer",
        color="#4169E1",
        image_file="thor.png"
    ),
    "freya": God(
        id="freya",
        culture=Culture.NORSE,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.95,
        intensity_level=0.65,
        gender="female",
        element="earth",
        domain="Love, Beauty, War, Magic",
        symbol="Falcon Cloak, Necklace Brisingamen",
        color="#FFD700",
        image_file="freya.png"
    ),
    "loki": God(
        id="loki",
        culture=Culture.NORSE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.6,
        intensity_level=0.8,
        gender="neutral",
        element="fire",
        domain="Trickery, Mischief, Chaos",
        symbol="Fire, Serpent",
        color="#FF4500",
        image_file="loki.png"
    ),
    "frigg": God(
        id="frigg",
        culture=Culture.NORSE,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="female",
        element="air",
        domain="Marriage, Motherhood, Fate",
        symbol="Spinning Wheel, Keys",
        color="#E6E6FA",
        image_file="frigg.png"
    ),
    "baldur": God(
        id="baldur",
        culture=Culture.NORSE,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.98,
        intensity_level=0.4,
        gender="male",
        element="fire",
        domain="Light, Purity, Joy",
        symbol="Mistletoe, Sun",
        color="#FFFACD",
        image_file="baldur.png"
    ),
    "tyr": God(
        id="tyr",
        culture=Culture.NORSE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="male",
        element="air",
        domain="War, Justice, Honor",
        symbol="Sword, One Hand",
        color="#B22222",
        image_file="tyr.png"
    ),
    "hel": God(
        id="hel",
        culture=Culture.NORSE,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.DEEP, EyeType.NARROW],
        symmetry_preference=0.5,
        intensity_level=0.9,
        gender="female",
        element="earth",
        domain="Underworld, Death",
        symbol="Half-living face",
        color="#2F4F4F",
        image_file="hel.png"
    ),

    # ============================================
    # EGYPTIAN MYTHOLOGY (이집트 신화)
    # ============================================
    "ra": God(
        id="ra",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Sun, Creation, King of Gods",
        symbol="Sun Disk, Falcon",
        color="#FFD700",
        image_file="ra.png"
    ),
    "isis": God(
        id="isis",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="female",
        element="water",
        domain="Magic, Motherhood, Healing",
        symbol="Throne, Wings",
        color="#1E90FF",
        image_file="isis.png"
    ),
    "osiris": God(
        id="osiris",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.7,
        gender="male",
        element="earth",
        domain="Underworld, Resurrection, Agriculture",
        symbol="Crook and Flail, Green Skin",
        color="#228B22",
        image_file="osiris.png"
    ),
    "anubis": God(
        id="anubis",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.85,
        gender="male",
        element="earth",
        domain="Mummification, Afterlife, Judgment",
        symbol="Jackal Head, Scales",
        color="#000000",
        image_file="anubis.png"
    ),
    "horus": God(
        id="horus",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="air",
        domain="Sky, Kingship, Protection",
        symbol="Eye of Horus, Falcon",
        color="#4169E1",
        image_file="horus.png"
    ),
    "bastet": God(
        id="bastet",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="female",
        element="fire",
        domain="Cats, Home, Fertility",
        symbol="Cat, Sistrum",
        color="#DEB887",
        image_file="bastet.png"
    ),
    "sekhmet": God(
        id="sekhmet",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.8,
        intensity_level=0.95,
        gender="female",
        element="fire",
        domain="War, Healing, Destruction",
        symbol="Lioness, Sun Disk",
        color="#DC143C",
        image_file="sekhmet.png"
    ),
    "thoth": God(
        id="thoth",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="male",
        element="air",
        domain="Wisdom, Writing, Magic, Moon",
        symbol="Ibis, Scroll",
        color="#C0C0C0",
        image_file="thoth.png"
    ),
    "set": God(
        id="set",
        culture=Culture.EGYPTIAN,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.7,
        intensity_level=0.9,
        gender="male",
        element="earth",
        domain="Chaos, Desert, Storms",
        symbol="Set Animal, Was Scepter",
        color="#8B4513",
        image_file="set.png"
    ),

    # ============================================
    # HINDU MYTHOLOGY (힌두 신화)
    # ============================================
    "shiva": God(
        id="shiva",
        culture=Culture.HINDU,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Destruction, Transformation, Dance",
        symbol="Trident, Third Eye, Crescent Moon",
        color="#4169E1",
        image_file="shiva.png"
    ),
    "vishnu": God(
        id="vishnu",
        culture=Culture.HINDU,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="male",
        element="water",
        domain="Preservation, Protection, Order",
        symbol="Conch, Discus, Lotus",
        color="#1E90FF",
        image_file="vishnu.png"
    ),
    "brahma": God(
        id="brahma",
        culture=Culture.HINDU,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="male",
        element="air",
        domain="Creation, Knowledge, Vedas",
        symbol="Four Heads, Lotus, Vedas",
        color="#FFD700",
        image_file="brahma.png"
    ),
    "ganesha": God(
        id="ganesha",
        culture=Culture.HINDU,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.5,
        gender="male",
        element="earth",
        domain="Wisdom, Success, New Beginnings",
        symbol="Elephant Head, Broken Tusk",
        color="#FF8C00",
        image_file="ganesha.png"
    ),
    "lakshmi": God(
        id="lakshmi",
        culture=Culture.HINDU,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.98,
        intensity_level=0.4,
        gender="female",
        element="water",
        domain="Wealth, Fortune, Beauty",
        symbol="Lotus, Gold Coins",
        color="#FFD700",
        image_file="lakshmi.png"
    ),
    "saraswati": God(
        id="saraswati",
        culture=Culture.HINDU,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Knowledge, Music, Arts",
        symbol="Veena, Swan, Books",
        color="#FFFFFF",
        image_file="saraswati.png"
    ),
    "kali": God(
        id="kali",
        culture=Culture.HINDU,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.SHARP, EyeType.WIDE],
        symmetry_preference=0.7,
        intensity_level=0.98,
        gender="female",
        element="fire",
        domain="Time, Death, Liberation",
        symbol="Sword, Severed Head, Tongue",
        color="#000000",
        image_file="kali.png"
    ),
    "durga": God(
        id="durga",
        culture=Culture.HINDU,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="female",
        element="fire",
        domain="War, Protection, Strength",
        symbol="Lion, Multiple Arms, Weapons",
        color="#DC143C",
        image_file="durga.png"
    ),
    "hanuman": God(
        id="hanuman",
        culture=Culture.HINDU,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="male",
        element="air",
        domain="Devotion, Strength, Courage",
        symbol="Monkey Face, Mace",
        color="#FF8C00",
        image_file="hanuman.png"
    ),
    "krishna": God(
        id="krishna",
        culture=Culture.HINDU,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="male",
        element="water",
        domain="Love, Wisdom, Mischief",
        symbol="Flute, Peacock Feather",
        color="#4169E1",
        image_file="krishna.png"
    ),

    # ============================================
    # CHINESE MYTHOLOGY (중국 신화)
    # ============================================
    "jade_emperor": God(
        id="jade_emperor",
        culture=Culture.CHINESE,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.95,
        intensity_level=0.7,
        gender="male",
        element="air",
        domain="Heaven, King of All Gods",
        symbol="Imperial Robes, Dragon Throne",
        color="#FFD700",
        image_file="jade_emperor.png"
    ),
    "guanyin": God(
        id="guanyin",
        culture=Culture.CHINESE,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.98,
        intensity_level=0.3,
        gender="female",
        element="water",
        domain="Mercy, Compassion, Salvation",
        symbol="Lotus, Willow Branch, Vase",
        color="#FFFFFF",
        image_file="guanyin.png"
    ),
    "sun_wukong": God(
        id="sun_wukong",
        culture=Culture.CHINESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.7,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Trickery, Strength, Immortality",
        symbol="Golden Staff, Cloud",
        color="#FFD700",
        image_file="sun_wukong.png"
    ),
    "dragon_king": God(
        id="dragon_king",
        culture=Culture.CHINESE,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.85,
        gender="male",
        element="water",
        domain="Sea, Weather, Rain",
        symbol="Dragon, Pearl",
        color="#1E90FF",
        image_file="dragon_king.png"
    ),
    "guan_yu": God(
        id="guan_yu",
        culture=Culture.CHINESE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="War, Loyalty, Righteousness",
        symbol="Green Dragon Blade, Red Face",
        color="#DC143C",
        image_file="guan_yu.png"
    ),
    "nuwa": God(
        id="nuwa",
        culture=Culture.CHINESE,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="earth",
        domain="Creation, Humanity, Sky Repair",
        symbol="Serpent Tail, Five-colored Stones",
        color="#9370DB",
        image_file="nuwa.png"
    ),
    "erlang_shen": God(
        id="erlang_shen",
        culture=Culture.CHINESE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="air",
        domain="Warrior, Third Eye, Justice",
        symbol="Third Eye, Celestial Hound",
        color="#4169E1",
        image_file="erlang_shen.png"
    ),
    "nezha": God(
        id="nezha",
        culture=Culture.CHINESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.75,
        gender="male",
        element="fire",
        domain="Protection, Youth, Rebellion",
        symbol="Fire Wheels, Wind Fire Spear",
        color="#FF4500",
        image_file="nezha.png"
    ),

    # ============================================
    # JAPANESE MYTHOLOGY (일본 신화)
    # ============================================
    "amaterasu": God(
        id="amaterasu",
        culture=Culture.JAPANESE,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.98,
        intensity_level=0.6,
        gender="female",
        element="fire",
        domain="Sun, Universe, Imperial Ancestor",
        symbol="Mirror, Rising Sun",
        color="#FFD700",
        image_file="amaterasu.png"
    ),
    "tsukuyomi": God(
        id="tsukuyomi",
        culture=Culture.JAPANESE,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.6,
        gender="male",
        element="water",
        domain="Moon, Night",
        symbol="Crescent Moon",
        color="#C0C0C0",
        image_file="tsukuyomi.png"
    ),
    "susanoo": God(
        id="susanoo",
        culture=Culture.JAPANESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.WIDE],
        symmetry_preference=0.75,
        intensity_level=0.9,
        gender="male",
        element="water",
        domain="Sea, Storms, Chaos",
        symbol="Sword Kusanagi",
        color="#4169E1",
        image_file="susanoo.png"
    ),
    "inari": God(
        id="inari",
        culture=Culture.JAPANESE,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="neutral",
        element="earth",
        domain="Rice, Fertility, Foxes, Commerce",
        symbol="Fox, Rice, Torii Gate",
        color="#FF8C00",
        image_file="inari.png"
    ),
    "raijin": God(
        id="raijin",
        culture=Culture.JAPANESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.WIDE, EyeType.SHARP],
        symmetry_preference=0.7,
        intensity_level=0.9,
        gender="male",
        element="air",
        domain="Thunder, Lightning",
        symbol="Drums, Demon Appearance",
        color="#FFD700",
        image_file="raijin.png"
    ),
    "fujin": God(
        id="fujin",
        culture=Culture.JAPANESE,
        archetype=Archetype.EXPLORER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.WIDE, EyeType.BRIGHT],
        symmetry_preference=0.7,
        intensity_level=0.8,
        gender="male",
        element="air",
        domain="Wind",
        symbol="Wind Bag, Green Skin",
        color="#90EE90",
        image_file="fujin.png"
    ),
    "benzaiten": God(
        id="benzaiten",
        culture=Culture.JAPANESE,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Music, Arts, Knowledge, Love",
        symbol="Biwa (Lute), Snake, Water",
        color="#E6E6FA",
        image_file="benzaiten.png"
    ),
    "kitsune": God(
        id="kitsune",
        culture=Culture.JAPANESE,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.7,
        gender="neutral",
        element="fire",
        domain="Trickery, Magic, Shapeshifting",
        symbol="Fox, Nine Tails",
        color="#FFD700",
        image_file="kitsune.png"
    ),

    # ============================================
    # KOREAN MYTHOLOGY (한국 신화)
    # ============================================
    "hwanung": God(
        id="hwanung",
        culture=Culture.KOREAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.95,
        intensity_level=0.7,
        gender="male",
        element="air",
        domain="Heaven, Civilization",
        symbol="Divine Seal, Wind/Rain/Cloud",
        color="#FFD700",
        image_file="hwanung.png"
    ),
    "dangun": God(
        id="dangun",
        culture=Culture.KOREAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="male",
        element="earth",
        domain="First King, Ancestor",
        symbol="Bear, Tiger, Gojoseon",
        color="#8B4513",
        image_file="dangun.png"
    ),
    "gumiho": God(
        id="gumiho",
        culture=Culture.KOREAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.HEART, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="female",
        element="fire",
        domain="Transformation, Seduction, Magic",
        symbol="Nine-tailed Fox",
        color="#FF69B4",
        image_file="gumiho.png"
    ),
    "jacheongbi": God(
        id="jacheongbi",
        culture=Culture.KOREAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="female",
        element="earth",
        domain="Agriculture, Grains, Harvest",
        symbol="Seeds, Farming Tools",
        color="#228B22",
        image_file="jacheongbi.png"
    ),
    "mago": God(
        id="mago",
        culture=Culture.KOREAN,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="earth",
        domain="Creation, Earth Mother, Nature",
        symbol="Earth, Mountains",
        color="#8B4513",
        image_file="mago.png"
    ),
    "cheoyong": God(
        id="cheoyong",
        culture=Culture.KOREAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.8,
        intensity_level=0.7,
        gender="male",
        element="water",
        domain="Protection, Exorcism, Dance",
        symbol="Mask, Dance",
        color="#DC143C",
        image_file="cheoyong.png"
    ),
    "dokkaebi": God(
        id="dokkaebi",
        culture=Culture.KOREAN,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.6,
        intensity_level=0.7,
        gender="neutral",
        element="fire",
        domain="Mischief, Fortune, Trickery",
        symbol="Club, Horns, Fire",
        color="#4169E1",
        image_file="dokkaebi.png"
    ),
    "samsin": God(
        id="samsin",
        culture=Culture.KOREAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.9,
        intensity_level=0.4,
        gender="female",
        element="water",
        domain="Birth, Fertility, Children",
        symbol="Three Grandmothers, Baby",
        color="#FFB6C1",
        image_file="samsin.png"
    ),

    # ============================================
    # CELTIC MYTHOLOGY (켈트 신화)
    # ============================================
    "dagda": God(
        id="dagda",
        culture=Culture.CELTIC,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.SQUARE],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.8,
        intensity_level=0.7,
        gender="male",
        element="earth",
        domain="Fertility, Agriculture, Wisdom",
        symbol="Cauldron, Club, Harp",
        color="#228B22",
        image_file="dagda.png"
    ),
    "morrigan": God(
        id="morrigan",
        culture=Culture.CELTIC,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.75,
        intensity_level=0.9,
        gender="female",
        element="air",
        domain="War, Fate, Death, Prophecy",
        symbol="Crow, Raven",
        color="#2F4F4F",
        image_file="morrigan.png"
    ),
    "brigid": God(
        id="brigid",
        culture=Culture.CELTIC,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.6,
        gender="female",
        element="fire",
        domain="Healing, Poetry, Smithcraft",
        symbol="Flame, Well, Brigid's Cross",
        color="#FF8C00",
        image_file="brigid.png"
    ),
    "lugh": God(
        id="lugh",
        culture=Culture.CELTIC,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Sun, Skill, Harvest",
        symbol="Spear, Sling",
        color="#FFD700",
        image_file="lugh.png"
    ),
    "cernunnos": God(
        id="cernunnos",
        culture=Culture.CELTIC,
        archetype=Archetype.EXPLORER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.85,
        intensity_level=0.7,
        gender="male",
        element="earth",
        domain="Nature, Animals, Underworld",
        symbol="Antlers, Torc, Serpent",
        color="#228B22",
        image_file="cernunnos.png"
    ),

    # ============================================
    # SLAVIC MYTHOLOGY (슬라브 신화)
    # ============================================
    "perun": God(
        id="perun",
        culture=Culture.SLAVIC,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="sky",
        domain="Thunder, Lightning, War, Law",
        symbol="Axe, Oak Tree, Eagle",
        color="#4169E1",
        image_file="perun.png"
    ),
    "veles": God(
        id="veles",
        culture=Culture.SLAVIC,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.NARROW],
        symmetry_preference=0.7,
        intensity_level=0.8,
        gender="male",
        element="water",
        domain="Underworld, Cattle, Magic",
        symbol="Serpent, Bear, Willow",
        color="#2F4F4F",
        image_file="veles.png"
    ),
    "morana": God(
        id="morana",
        culture=Culture.SLAVIC,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="female",
        element="water",
        domain="Winter, Death, Rebirth",
        symbol="Ice, Skull, Straw Effigy",
        color="#ADD8E6",
        image_file="morana.png"
    ),
    "svarog": God(
        id="svarog",
        culture=Culture.SLAVIC,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="male",
        element="fire",
        domain="Sky, Sun, Fire, Smithing",
        symbol="Forge, Fire, Sun",
        color="#FF8C00",
        image_file="svarog.png"
    ),
    "lada": God(
        id="lada",
        culture=Culture.SLAVIC,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.4,
        gender="female",
        element="water",
        domain="Love, Beauty, Spring",
        symbol="Swan, Flowers",
        color="#FFB6C1",
        image_file="lada.png"
    ),

    # ============================================
    # MESOPOTAMIAN/ARABIC MYTHOLOGY (메소포타미아/아랍 신화)
    # ============================================
    "marduk": God(
        id="marduk",
        culture=Culture.MESOPOTAMIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.9,
        gender="male",
        element="water",
        domain="Creation, Storm, Justice",
        symbol="Dragon, Spade",
        color="#4169E1",
        image_file="marduk.png"
    ),
    "ishtar": God(
        id="ishtar",
        culture=Culture.MESOPOTAMIAN,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.75,
        gender="female",
        element="air",
        domain="Love, War, Fertility",
        symbol="Eight-pointed Star, Lion",
        color="#FFD700",
        image_file="ishtar.png"
    ),
    "enlil": God(
        id="enlil",
        culture=Culture.MESOPOTAMIAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="male",
        element="air",
        domain="Wind, Air, Authority",
        symbol="Crown of Horns",
        color="#87CEEB",
        image_file="enlil.png"
    ),
    "jinn": God(
        id="jinn",
        culture=Culture.ARABIC,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.7,
        intensity_level=0.8,
        gender="neutral",
        element="fire",
        domain="Magic, Wishes, Smoke",
        symbol="Lamp, Smoke, Fire",
        color="#9370DB",
        image_file="jinn.png"
    ),

    # ============================================
    # SOUTHEAST ASIAN MYTHOLOGY (동남아 신화)
    # ============================================
    "naga": God(
        id="naga",
        culture=Culture.THAI,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.75,
        gender="neutral",
        element="water",
        domain="Water, Underworld, Protection",
        symbol="Serpent, Multiple Heads",
        color="#1E90FF",
        image_file="naga.png"
    ),
    "garuda": God(
        id="garuda",
        culture=Culture.THAI,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="male",
        element="air",
        domain="Sun, Sky, King of Birds",
        symbol="Eagle, Wings",
        color="#FFD700",
        image_file="garuda.png"
    ),
    "thao_maha_phrom": God(
        id="thao_maha_phrom",
        culture=Culture.THAI,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="male",
        element="air",
        domain="Creation, Fortune, Protection",
        symbol="Four Faces, Lotus",
        color="#FFD700",
        image_file="thao_maha_phrom.png"
    ),
    "son_tinh": God(
        id="son_tinh",
        culture=Culture.VIETNAMESE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="male",
        element="earth",
        domain="Mountains, Earth, Protection",
        symbol="Mountain, Dragon",
        color="#8B4513",
        image_file="son_tinh.png"
    ),
    "thuy_tinh": God(
        id="thuy_tinh",
        culture=Culture.VIETNAMESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.WIDE],
        symmetry_preference=0.75,
        intensity_level=0.85,
        gender="male",
        element="water",
        domain="Water, Sea, Storms",
        symbol="Waves, Sea Creatures",
        color="#1E90FF",
        image_file="thuy_tinh.png"
    ),
    "dewi_sri": God(
        id="dewi_sri",
        culture=Culture.INDONESIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.4,
        gender="female",
        element="earth",
        domain="Rice, Fertility, Agriculture",
        symbol="Rice, Serpent, Offerings",
        color="#228B22",
        image_file="dewi_sri.png"
    ),
    "barong": God(
        id="barong",
        culture=Culture.INDONESIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.WIDE, EyeType.BRIGHT],
        symmetry_preference=0.8,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Good, Protection, Light",
        symbol="Lion, Sacred Mask",
        color="#FFD700",
        image_file="barong.png"
    ),
    "rangda": God(
        id="rangda",
        culture=Culture.INDONESIAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.WIDE],
        symmetry_preference=0.6,
        intensity_level=0.95,
        gender="female",
        element="fire",
        domain="Darkness, Magic, Chaos",
        symbol="Witch, Fangs, Long Tongue",
        color="#2F4F4F",
        image_file="rangda.png"
    ),

    # ============================================
    # AZTEC MYTHOLOGY (아즈텍 신화)
    # ============================================
    "quetzalcoatl": God(
        id="quetzalcoatl",
        culture=Culture.AZTEC,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.9,
        intensity_level=0.7,
        gender="male",
        element="air",
        domain="Wind, Air, Learning, Civilization",
        symbol="Feathered Serpent",
        color="#00CED1",
        image_file="quetzalcoatl.png"
    ),
    "tezcatlipoca": God(
        id="tezcatlipoca",
        culture=Culture.AZTEC,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.75,
        intensity_level=0.95,
        gender="male",
        element="earth",
        domain="Night, Sorcery, Fate",
        symbol="Obsidian Mirror, Jaguar",
        color="#000000",
        image_file="tezcatlipoca.png"
    ),
    "huitzilopochtli": God(
        id="huitzilopochtli",
        culture=Culture.AZTEC,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Sun, War, Human Sacrifice",
        symbol="Hummingbird, Eagle",
        color="#FFD700",
        image_file="huitzilopochtli.png"
    ),
    "coatlicue": God(
        id="coatlicue",
        culture=Culture.AZTEC,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.WIDE],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="female",
        element="earth",
        domain="Earth, Life, Death, Fertility",
        symbol="Serpent Skirt, Skulls",
        color="#8B4513",
        image_file="coatlicue.png"
    ),

    # ============================================
    # CONFUCIAN SAGES (유교 현자)
    # ============================================
    "confucius": God(
        id="confucius",
        culture=Culture.CONFUCIAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="male",
        element="earth",
        domain="Ethics, Education, Social Harmony",
        symbol="Scroll, Brush, Scholar Robes",
        color="#8B4513",
        image_file="confucius.png"
    ),
    "mencius": God(
        id="mencius",
        culture=Culture.CONFUCIAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.45,
        gender="male",
        element="water",
        domain="Human Nature, Benevolence",
        symbol="Four Books, Jade",
        color="#228B22",
        image_file="mencius.png"
    ),
    "zhuxi": God(
        id="zhuxi",
        culture=Culture.CONFUCIAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.55,
        gender="male",
        element="fire",
        domain="Neo-Confucianism, Philosophy",
        symbol="Yin-Yang, Books",
        color="#4169E1",
        image_file="zhuxi.png"
    ),

    # ============================================
    # TAOIST SAGES (도교 현자)
    # ============================================
    "laozi": God(
        id="laozi",
        culture=Culture.TAOIST,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.4,
        gender="male",
        element="water",
        domain="Tao, Natural Way, Wu Wei",
        symbol="Ox, Tao Te Ching, Gourd",
        color="#000000",
        image_file="laozi.png"
    ),
    "zhuangzi": God(
        id="zhuangzi",
        culture=Culture.TAOIST,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.75,
        intensity_level=0.5,
        gender="male",
        element="air",
        domain="Freedom, Dreams, Paradox",
        symbol="Butterfly, Fish",
        color="#87CEEB",
        image_file="zhuangzi.png"
    ),
    "zhang_daoling": God(
        id="zhang_daoling",
        culture=Culture.TAOIST,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.7,
        gender="male",
        element="fire",
        domain="Exorcism, Talismans, Celestial Masters",
        symbol="Tiger, Sword, Talisman",
        color="#FFD700",
        image_file="zhang_daoling.png"
    ),
    "eight_immortals_lu": God(
        id="eight_immortals_lu",
        culture=Culture.TAOIST,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.65,
        gender="male",
        element="air",
        domain="Alchemy, Immortality, Swordsmanship",
        symbol="Sword, Fly-whisk",
        color="#4169E1",
        image_file="lu_dongbin.png"
    ),

    # ============================================
    # BUDDHIST FIGURES (불교 인물)
    # ============================================
    "buddha": God(
        id="buddha",
        culture=Culture.BUDDHIST,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.98,
        intensity_level=0.3,
        gender="male",
        element="earth",
        domain="Enlightenment, Compassion, Middle Way",
        symbol="Lotus, Bodhi Tree, Dharma Wheel",
        color="#FFD700",
        image_file="buddha.png"
    ),
    "avalokiteshvara": God(
        id="avalokiteshvara",
        culture=Culture.BUDDHIST,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.95,
        intensity_level=0.35,
        gender="neutral",
        element="water",
        domain="Compassion, Mercy, Salvation",
        symbol="Thousand Arms, Lotus, Vase",
        color="#FFFFFF",
        image_file="avalokiteshvara.png"
    ),
    "maitreya": God(
        id="maitreya",
        culture=Culture.BUDDHIST,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.4,
        gender="male",
        element="air",
        domain="Future Buddha, Hope, Joy",
        symbol="Stupa, Dharma Wheel",
        color="#FFD700",
        image_file="maitreya.png"
    ),
    "bodhidharma": God(
        id="bodhidharma",
        culture=Culture.BUDDHIST,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Zen, Meditation, Martial Arts",
        symbol="Red Robe, Piercing Eyes, Wall",
        color="#DC143C",
        image_file="bodhidharma.png"
    ),
    "wonhyo": God(
        id="wonhyo",
        culture=Culture.BUDDHIST,
        archetype=Archetype.EXPLORER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.85,
        intensity_level=0.6,
        gender="male",
        element="water",
        domain="Unification, Enlightenment, Korean Buddhism",
        symbol="Gourd, Dancing",
        color="#9370DB",
        image_file="wonhyo.png"
    ),
    "nichiren": God(
        id="nichiren",
        culture=Culture.BUDDHIST,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Devotion, Lotus Sutra, Japanese Buddhism",
        symbol="Scroll, Drum",
        color="#FF8C00",
        image_file="nichiren.png"
    ),

    # ============================================
    # CHRISTIAN SAINTS & FIGURES (기독교 성인)
    # ============================================
    "saint_michael": God(
        id="saint_michael",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Protection, Justice, Warrior Angel",
        symbol="Sword, Scales, Dragon",
        color="#FFD700",
        image_file="saint_michael.png"
    ),
    "saint_gabriel": God(
        id="saint_gabriel",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="neutral",
        element="air",
        domain="Messages, Revelation, Annunciation",
        symbol="Trumpet, Lily, Scroll",
        color="#FFFFFF",
        image_file="saint_gabriel.png"
    ),
    "saint_raphael": God(
        id="saint_raphael",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="male",
        element="water",
        domain="Healing, Journey, Protection",
        symbol="Staff, Fish, Healing",
        color="#228B22",
        image_file="saint_raphael.png"
    ),
    "virgin_mary": God(
        id="virgin_mary",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.98,
        intensity_level=0.35,
        gender="female",
        element="water",
        domain="Motherhood, Purity, Intercession",
        symbol="Blue Robe, Crown, Roses",
        color="#4169E1",
        image_file="virgin_mary.png"
    ),
    "saint_peter": God(
        id="saint_peter",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.EVERYMAN,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.8,
        intensity_level=0.65,
        gender="male",
        element="water",
        domain="Faith, Church Foundation, Keys to Heaven",
        symbol="Keys, Upside-down Cross",
        color="#FFD700",
        image_file="saint_peter.png"
    ),
    "saint_paul": God(
        id="saint_paul",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Conversion, Missionary Work, Theology",
        symbol="Sword, Letters, Book",
        color="#DC143C",
        image_file="saint_paul.png"
    ),
    "saint_francis": God(
        id="saint_francis",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.4,
        gender="male",
        element="earth",
        domain="Nature, Animals, Poverty, Peace",
        symbol="Birds, Wolf, Brown Robe",
        color="#8B4513",
        image_file="saint_francis.png"
    ),
    "saint_george": God(
        id="saint_george",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Chivalry, Dragon Slayer, Courage",
        symbol="Dragon, Lance, Red Cross",
        color="#DC143C",
        image_file="saint_george.png"
    ),
    "saint_joan_of_arc": God(
        id="saint_joan_of_arc",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.85,
        gender="female",
        element="fire",
        domain="Visions, Warfare, Martyrdom",
        symbol="Armor, Sword, Banner",
        color="#4169E1",
        image_file="saint_joan_of_arc.png"
    ),
    "saint_patrick": God(
        id="saint_patrick",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.85,
        intensity_level=0.6,
        gender="male",
        element="earth",
        domain="Ireland, Conversion, Snakes",
        symbol="Shamrock, Bishop Staff, Snakes",
        color="#228B22",
        image_file="saint_patrick.png"
    ),
    "saint_nicholas": God(
        id="saint_nicholas",
        culture=Culture.CHRISTIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.5,
        gender="male",
        element="water",
        domain="Children, Gifts, Generosity",
        symbol="Three Gold Balls, Bishop Robe",
        color="#DC143C",
        image_file="saint_nicholas.png"
    ),

    # ============================================
    # ISLAMIC FIGURES (이슬람 인물)
    # ============================================
    "prophet_muhammad": God(
        id="prophet_muhammad",
        culture=Culture.ISLAMIC,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.95,
        intensity_level=0.7,
        gender="male",
        element="fire",
        domain="Prophecy, Revelation, Leadership",
        symbol="Crescent Moon, Green",
        color="#228B22",
        image_file="prophet_silhouette.png"
    ),
    "ali_ibn_abi_talib": God(
        id="ali_ibn_abi_talib",
        culture=Culture.ISLAMIC,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Justice, Wisdom, Bravery",
        symbol="Zulfiqar Sword, Lion",
        color="#228B22",
        image_file="ali_silhouette.png"
    ),
    "rumi": God(
        id="rumi",
        culture=Culture.ISLAMIC,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="male",
        element="air",
        domain="Poetry, Love, Sufi Mysticism",
        symbol="Whirling Dervish, Flute",
        color="#9370DB",
        image_file="rumi.png"
    ),
    "saladin": God(
        id="saladin",
        culture=Culture.ISLAMIC,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="earth",
        domain="Chivalry, Justice, Military Leadership",
        symbol="Sword, Crescent, Eagle",
        color="#FFD700",
        image_file="saladin.png"
    ),
    "avicenna": God(
        id="avicenna",
        culture=Culture.ISLAMIC,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.6,
        gender="male",
        element="air",
        domain="Medicine, Philosophy, Science",
        symbol="Medical Book, Herbs",
        color="#4169E1",
        image_file="avicenna.png"
    ),

    # ============================================
    # GREEK PHILOSOPHERS (그리스 철학자)
    # ============================================
    "socrates": God(
        id="socrates",
        culture=Culture.GREEK,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.BRIGHT],
        symmetry_preference=0.75,
        intensity_level=0.65,
        gender="male",
        element="air",
        domain="Philosophy, Ethics, Questioning",
        symbol="Hemlock Cup, Dialogue",
        color="#708090",
        image_file="socrates.png"
    ),
    "plato": God(
        id="plato",
        culture=Culture.GREEK,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.6,
        gender="male",
        element="air",
        domain="Forms, Republic, Academy",
        symbol="Cave, Dialogue Scrolls",
        color="#4169E1",
        image_file="plato.png"
    ),
    "aristotle": God(
        id="aristotle",
        culture=Culture.GREEK,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.65,
        gender="male",
        element="earth",
        domain="Logic, Science, Ethics",
        symbol="Lyceum, Natural Objects",
        color="#8B4513",
        image_file="aristotle.png"
    ),
    "pythagoras": God(
        id="pythagoras",
        culture=Culture.GREEK,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.DEEP],
        symmetry_preference=0.95,
        intensity_level=0.7,
        gender="male",
        element="fire",
        domain="Mathematics, Music, Mysticism",
        symbol="Tetraktys, Lyre",
        color="#FFD700",
        image_file="pythagoras.png"
    ),
    "hippocrates": God(
        id="hippocrates",
        culture=Culture.GREEK,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.55,
        gender="male",
        element="water",
        domain="Medicine, Healing, Ethics",
        symbol="Staff of Asclepius, Herbs",
        color="#228B22",
        image_file="hippocrates.png"
    ),
    "alexander_the_great": God(
        id="alexander_the_great",
        culture=Culture.GREEK,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Conquest, Empire, Hellenism",
        symbol="Macedonian Star, Horse Bucephalus",
        color="#FFD700",
        image_file="alexander.png"
    ),
    "leonidas": God(
        id="leonidas",
        culture=Culture.GREEK,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Spartan Valor, Sacrifice, Leadership",
        symbol="Spartan Shield, Spear",
        color="#DC143C",
        image_file="leonidas.png"
    ),

    # ============================================
    # CHINESE HISTORICAL FIGURES (중국 역사 인물)
    # ============================================
    "zhuge_liang": God(
        id="zhuge_liang",
        culture=Culture.CHINESE,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="male",
        element="air",
        domain="Strategy, Wisdom, Invention",
        symbol="Feather Fan, Lantern",
        color="#228B22",
        image_file="zhuge_liang.png"
    ),
    "liu_bei": God(
        id="liu_bei",
        culture=Culture.CHINESE,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.6,
        gender="male",
        element="water",
        domain="Benevolence, Brotherhood, Virtue",
        symbol="Double Sword, Imperial Robe",
        color="#FFD700",
        image_file="liu_bei.png"
    ),
    "zhang_fei": God(
        id="zhang_fei",
        culture=Culture.CHINESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.WIDE, EyeType.SHARP],
        symmetry_preference=0.7,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Fierce Loyalty, Battle Prowess",
        symbol="Serpent Spear, Black Face",
        color="#000000",
        image_file="zhang_fei.png"
    ),
    "cao_cao": God(
        id="cao_cao",
        culture=Culture.CHINESE,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Ambition, Poetry, Cunning",
        symbol="Sword, Scroll",
        color="#4169E1",
        image_file="cao_cao.png"
    ),
    "qin_shi_huang": God(
        id="qin_shi_huang",
        culture=Culture.CHINESE,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.95,
        gender="male",
        element="earth",
        domain="Unification, Empire, Great Wall",
        symbol="Terracotta Warriors, Dragon",
        color="#FFD700",
        image_file="qin_shi_huang.png"
    ),
    "mulan": God(
        id="mulan",
        culture=Culture.CHINESE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="female",
        element="fire",
        domain="Filial Piety, Bravery, Disguise",
        symbol="Sword, Armor, Magnolia",
        color="#DC143C",
        image_file="mulan.png"
    ),
    "xu_xian": God(
        id="xu_xian",
        culture=Culture.CHINESE,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.4,
        gender="male",
        element="water",
        domain="True Love, Innocence, Devotion",
        symbol="White Snake, Umbrella",
        color="#FFFFFF",
        image_file="xu_xian.png"
    ),
    "white_snake": God(
        id="white_snake",
        culture=Culture.CHINESE,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="female",
        element="water",
        domain="Eternal Love, Transformation, Sacrifice",
        symbol="White Serpent, Umbrella",
        color="#FFFFFF",
        image_file="white_snake.png"
    ),

    # ============================================
    # JAPANESE HISTORICAL FIGURES (일본 역사 인물)
    # ============================================
    "miyamoto_musashi": God(
        id="miyamoto_musashi",
        culture=Culture.JAPANESE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Swordsmanship, Strategy, Art",
        symbol="Two Swords, Book of Five Rings",
        color="#2F4F4F",
        image_file="musashi.png"
    ),
    "oda_nobunaga": God(
        id="oda_nobunaga",
        culture=Culture.JAPANESE,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Unification, Innovation, Ambition",
        symbol="Oda Crest, Arquebus",
        color="#000000",
        image_file="nobunaga.png"
    ),
    "toyotomi_hideyoshi": God(
        id="toyotomi_hideyoshi",
        culture=Culture.JAPANESE,
        archetype=Archetype.EVERYMAN,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.8,
        intensity_level=0.8,
        gender="male",
        element="earth",
        domain="Rise from Peasant, Unification",
        symbol="Gourd Banner, Golden Armor",
        color="#FFD700",
        image_file="hideyoshi.png"
    ),
    "tokugawa_ieyasu": God(
        id="tokugawa_ieyasu",
        culture=Culture.JAPANESE,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.7,
        gender="male",
        element="water",
        domain="Patience, Dynasty, Peace",
        symbol="Tokugawa Crest, Tanuki",
        color="#228B22",
        image_file="ieyasu.png"
    ),
    "tomoe_gozen": God(
        id="tomoe_gozen",
        culture=Culture.JAPANESE,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="female",
        element="fire",
        domain="Female Warrior, Archery, Beauty",
        symbol="Naginata, Horse",
        color="#DC143C",
        image_file="tomoe_gozen.png"
    ),
    "abe_no_seimei": God(
        id="abe_no_seimei",
        culture=Culture.JAPANESE,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="male",
        element="air",
        domain="Onmyodo, Divination, Exorcism",
        symbol="Pentagram, Shikigami",
        color="#9370DB",
        image_file="seimei.png"
    ),

    # ============================================
    # KOREAN HISTORICAL FIGURES (한국 역사 인물)
    # ============================================
    "admiral_yi": God(
        id="admiral_yi",
        culture=Culture.KOREAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.9,
        gender="male",
        element="water",
        domain="Naval Warfare, Genius Strategy, Loyalty",
        symbol="Turtle Ship, Sword",
        color="#4169E1",
        image_file="admiral_yi.png"
    ),
    "sejong_the_great": God(
        id="sejong_the_great",
        culture=Culture.KOREAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.6,
        gender="male",
        element="air",
        domain="Hangul, Science, Benevolent Rule",
        symbol="Hangul Letters, Sundial",
        color="#FFD700",
        image_file="sejong.png"
    ),
    "jumong": God(
        id="jumong",
        culture=Culture.KOREAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Archery, Kingdom Founding, Destiny",
        symbol="Bow and Arrow, Horse",
        color="#DC143C",
        image_file="jumong.png"
    ),
    "hwang_jini": God(
        id="hwang_jini",
        culture=Culture.KOREAN,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="female",
        element="water",
        domain="Poetry, Dance, Beauty, Art",
        symbol="Gayageum, Moon",
        color="#FF69B4",
        image_file="hwang_jini.png"
    ),
    "gwanggaeto": God(
        id="gwanggaeto",
        culture=Culture.KOREAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Conquest, Expansion, Goguryeo Glory",
        symbol="Stele, Horse, Sword",
        color="#FFD700",
        image_file="gwanggaeto.png"
    ),
    "seon_deok": God(
        id="seon_deok",
        culture=Culture.KOREAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.7,
        gender="female",
        element="air",
        domain="First Queen Regnant, Astronomy, Wisdom",
        symbol="Cheomseongdae, Crown",
        color="#9370DB",
        image_file="seon_deok.png"
    ),

    # ============================================
    # PERSIAN MYTHOLOGY (페르시아 신화)
    # ============================================
    "ahura_mazda": God(
        id="ahura_mazda",
        culture=Culture.PERSIAN,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.98,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Light, Truth, Creation",
        symbol="Faravahar, Sacred Fire",
        color="#FFD700",
        image_file="ahura_mazda.png"
    ),
    "anahita": God(
        id="anahita",
        culture=Culture.PERSIAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Fertility, Water, Wisdom",
        symbol="Water, Pomegranate, Lion",
        color="#1E90FF",
        image_file="anahita.png"
    ),
    "mithra": God(
        id="mithra",
        culture=Culture.PERSIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Covenant, Light, Sun",
        symbol="Sun, Bull-slaying",
        color="#FFD700",
        image_file="mithra.png"
    ),
    "rostam": God(
        id="rostam",
        culture=Culture.PERSIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Epic Hero, Seven Labors, Strength",
        symbol="Horse Rakhsh, Mace",
        color="#DC143C",
        image_file="rostam.png"
    ),
    "cyrus_the_great": God(
        id="cyrus_the_great",
        culture=Culture.PERSIAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="air",
        domain="Human Rights, Empire, Tolerance",
        symbol="Cyrus Cylinder, Winged Lion",
        color="#FFD700",
        image_file="cyrus.png"
    ),

    # ============================================
    # AFRICAN MYTHOLOGY (아프리카 신화)
    # ============================================
    "anansi": God(
        id="anansi",
        culture=Culture.AFRICAN,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.7,
        intensity_level=0.7,
        gender="male",
        element="air",
        domain="Wisdom, Stories, Trickery",
        symbol="Spider, Web",
        color="#000000",
        image_file="anansi.png"
    ),
    "shango": God(
        id="shango",
        culture=Culture.AFRICAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="Thunder, Lightning, Justice",
        symbol="Double Axe, Drums",
        color="#DC143C",
        image_file="shango.png"
    ),
    "oshun": God(
        id="oshun",
        culture=Culture.AFRICAN,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Love, Beauty, Rivers, Fertility",
        symbol="Mirror, Fan, Gold",
        color="#FFD700",
        image_file="oshun.png"
    ),
    "yemoja": God(
        id="yemoja",
        culture=Culture.AFRICAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Ocean, Motherhood, Children",
        symbol="Seashells, Fish, Blue",
        color="#1E90FF",
        image_file="yemoja.png"
    ),
    "ogun": God(
        id="ogun",
        culture=Culture.AFRICAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.8,
        intensity_level=0.9,
        gender="male",
        element="fire",
        domain="Iron, War, Labor, Technology",
        symbol="Machete, Anvil",
        color="#2F4F4F",
        image_file="ogun.png"
    ),
    "mami_wata": God(
        id="mami_wata",
        culture=Culture.AFRICAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="female",
        element="water",
        domain="Water, Wealth, Healing, Beauty",
        symbol="Snake, Mirror, Comb",
        color="#00CED1",
        image_file="mami_wata.png"
    ),

    # ============================================
    # POLYNESIAN MYTHOLOGY (폴리네시아 신화)
    # ============================================
    "maui": God(
        id="maui",
        culture=Culture.POLYNESIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.ROUND],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.8,
        intensity_level=0.8,
        gender="male",
        element="fire",
        domain="Trickster Hero, Islands, Sun",
        symbol="Fishhook, Tattoos",
        color="#8B4513",
        image_file="maui.png"
    ),
    "pele": God(
        id="pele",
        culture=Culture.POLYNESIAN,
        archetype=Archetype.REBEL,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.75,
        intensity_level=0.95,
        gender="female",
        element="fire",
        domain="Volcanoes, Fire, Lightning",
        symbol="Volcano, Lava, Ohia Flower",
        color="#FF4500",
        image_file="pele.png"
    ),
    "tangaroa": God(
        id="tangaroa",
        culture=Culture.POLYNESIAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="male",
        element="water",
        domain="Sea, Fish, Creator",
        symbol="Octopus, Fish, Waves",
        color="#1E90FF",
        image_file="tangaroa.png"
    ),
    "hina": God(
        id="hina",
        culture=Culture.POLYNESIAN,
        archetype=Archetype.CREATOR,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Moon, Weaving, Women",
        symbol="Moon, Tapa Cloth",
        color="#C0C0C0",
        image_file="hina.png"
    ),

    # ============================================
    # NATIVE AMERICAN MYTHOLOGY (아메리카 원주민 신화)
    # ============================================
    "coyote": God(
        id="coyote",
        culture=Culture.NATIVE_AMERICAN,
        archetype=Archetype.JESTER,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.65,
        intensity_level=0.7,
        gender="male",
        element="air",
        domain="Trickster, Creation, Teaching",
        symbol="Coyote, Desert",
        color="#DEB887",
        image_file="coyote.png"
    ),
    "white_buffalo_woman": God(
        id="white_buffalo_woman",
        culture=Culture.NATIVE_AMERICAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="female",
        element="earth",
        domain="Sacred Pipe, Spirituality, Buffalo",
        symbol="White Buffalo, Sacred Pipe",
        color="#FFFFFF",
        image_file="white_buffalo_woman.png"
    ),
    "thunderbird": God(
        id="thunderbird",
        culture=Culture.NATIVE_AMERICAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.9,
        gender="male",
        element="air",
        domain="Thunder, Storms, Power",
        symbol="Giant Bird, Lightning",
        color="#4169E1",
        image_file="thunderbird.png"
    ),
    "spider_grandmother": God(
        id="spider_grandmother",
        culture=Culture.NATIVE_AMERICAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.ROUND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.45,
        gender="female",
        element="earth",
        domain="Creation, Weaving, Guidance",
        symbol="Spider, Web, Pottery",
        color="#8B4513",
        image_file="spider_grandmother.png"
    ),

    # ============================================
    # MAYAN MYTHOLOGY (마야 신화)
    # ============================================
    "kukulkan": God(
        id="kukulkan",
        culture=Culture.MAYAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.WIDE],
        symmetry_preference=0.9,
        intensity_level=0.75,
        gender="male",
        element="air",
        domain="Wind, Learning, Civilization",
        symbol="Feathered Serpent, Pyramid",
        color="#00CED1",
        image_file="kukulkan.png"
    ),
    "ixchel": God(
        id="ixchel",
        culture=Culture.MAYAN,
        archetype=Archetype.CAREGIVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.85,
        intensity_level=0.55,
        gender="female",
        element="water",
        domain="Moon, Fertility, Medicine",
        symbol="Rabbit, Snake, Water Jar",
        color="#C0C0C0",
        image_file="ixchel.png"
    ),
    "chaac": God(
        id="chaac",
        culture=Culture.MAYAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.WIDE],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="male",
        element="water",
        domain="Rain, Thunder, Agriculture",
        symbol="Axe, Lightning, Jade",
        color="#1E90FF",
        image_file="chaac.png"
    ),
    "hun_hunahpu": God(
        id="hun_hunahpu",
        culture=Culture.MAYAN,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.ROUND],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.9,
        intensity_level=0.5,
        gender="male",
        element="earth",
        domain="Maize, Sacrifice, Rebirth",
        symbol="Maize, Ballgame",
        color="#FFD700",
        image_file="hun_hunahpu.png"
    ),

    # ============================================
    # ARTHURIAN LEGEND (아서왕 전설)
    # ============================================
    "king_arthur": God(
        id="king_arthur",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.SOFT],
        symmetry_preference=0.9,
        intensity_level=0.8,
        gender="male",
        element="earth",
        domain="Kingship, Chivalry, Camelot",
        symbol="Excalibur, Round Table, Crown",
        color="#FFD700",
        image_file="king_arthur.png"
    ),
    "merlin": God(
        id="merlin",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OBLONG, FaceShape.OVAL],
        preferred_eye_types=[EyeType.DEEP, EyeType.BRIGHT],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="male",
        element="air",
        domain="Magic, Prophecy, Wisdom",
        symbol="Staff, Owl, Crystal",
        color="#4B0082",
        image_file="merlin.png"
    ),
    "guinevere": God(
        id="guinevere",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.DEEP],
        symmetry_preference=0.95,
        intensity_level=0.5,
        gender="female",
        element="water",
        domain="Beauty, Love, Tragedy",
        symbol="Crown, Rose",
        color="#FFB6C1",
        image_file="guinevere.png"
    ),
    "lancelot": God(
        id="lancelot",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.9,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Greatest Knight, Love, Tragedy",
        symbol="White Shield, Sword",
        color="#C0C0C0",
        image_file="lancelot.png"
    ),
    "morgan_le_fay": God(
        id="morgan_le_fay",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.DIAMOND, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.8,
        gender="female",
        element="water",
        domain="Magic, Healing, Avalon",
        symbol="Apple, Raven, Mist",
        color="#9370DB",
        image_file="morgan_le_fay.png"
    ),
    "lady_of_the_lake": God(
        id="lady_of_the_lake",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.WIZARD,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.6,
        gender="female",
        element="water",
        domain="Magic, Excalibur, Otherworld",
        symbol="Lake, Sword, Mist",
        color="#1E90FF",
        image_file="lady_of_the_lake.png"
    ),
    "galahad": God(
        id="galahad",
        culture=Culture.ARTHURIAN,
        archetype=Archetype.INNOCENT,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.BRIGHT, EyeType.SOFT],
        symmetry_preference=0.98,
        intensity_level=0.5,
        gender="male",
        element="air",
        domain="Purity, Holy Grail, Perfection",
        symbol="White Shield, Red Cross, Grail",
        color="#FFFFFF",
        image_file="galahad.png"
    ),

    # ============================================
    # ROMAN MYTHOLOGY (로마 신화)
    # ============================================
    "jupiter": God(
        id="jupiter",
        culture=Culture.ROMAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.SHARP],
        symmetry_preference=0.9,
        intensity_level=0.9,
        gender="male",
        element="sky",
        domain="King of Gods, Sky, Thunder",
        symbol="Eagle, Thunderbolt",
        color="#FFD700",
        image_file="jupiter.png"
    ),
    "mars": God(
        id="mars",
        culture=Culture.ROMAN,
        archetype=Archetype.HERO,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.NARROW],
        symmetry_preference=0.85,
        intensity_level=0.95,
        gender="male",
        element="fire",
        domain="War, Agriculture, Guardian",
        symbol="Spear, Shield, Wolf",
        color="#DC143C",
        image_file="mars.png"
    ),
    "venus": God(
        id="venus",
        culture=Culture.ROMAN,
        archetype=Archetype.LOVER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SOFT, EyeType.WIDE],
        symmetry_preference=0.98,
        intensity_level=0.45,
        gender="female",
        element="water",
        domain="Love, Beauty, Prosperity",
        symbol="Mirror, Dove, Myrtle",
        color="#FFB6C1",
        image_file="venus.png"
    ),
    "minerva": God(
        id="minerva",
        culture=Culture.ROMAN,
        archetype=Archetype.SAGE,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.DIAMOND],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.95,
        intensity_level=0.7,
        gender="female",
        element="air",
        domain="Wisdom, Strategic Warfare, Arts",
        symbol="Owl, Spear, Aegis",
        color="#708090",
        image_file="minerva.png"
    ),
    "neptune": God(
        id="neptune",
        culture=Culture.ROMAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.DEEP, EyeType.WIDE],
        symmetry_preference=0.8,
        intensity_level=0.85,
        gender="male",
        element="water",
        domain="Sea, Earthquakes, Horses",
        symbol="Trident, Horse, Dolphin",
        color="#1E90FF",
        image_file="neptune.png"
    ),
    "diana": God(
        id="diana",
        culture=Culture.ROMAN,
        archetype=Archetype.EXPLORER,
        preferred_face_shapes=[FaceShape.HEART, FaceShape.OVAL],
        preferred_eye_types=[EyeType.SHARP, EyeType.BRIGHT],
        symmetry_preference=0.85,
        intensity_level=0.75,
        gender="female",
        element="earth",
        domain="Hunt, Moon, Nature",
        symbol="Bow and Arrow, Deer, Moon",
        color="#C0C0C0",
        image_file="diana.png"
    ),
    "juno": God(
        id="juno",
        culture=Culture.ROMAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.OVAL, FaceShape.HEART],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.95,
        intensity_level=0.8,
        gender="female",
        element="air",
        domain="Marriage, Childbirth, Queen of Gods",
        symbol="Peacock, Diadem",
        color="#800080",
        image_file="juno.png"
    ),
    "romulus": God(
        id="romulus",
        culture=Culture.ROMAN,
        archetype=Archetype.RULER,
        preferred_face_shapes=[FaceShape.SQUARE, FaceShape.OBLONG],
        preferred_eye_types=[EyeType.SHARP, EyeType.DEEP],
        symmetry_preference=0.85,
        intensity_level=0.85,
        gender="male",
        element="fire",
        domain="Rome's Founder, Warrior King",
        symbol="Wolf, Spear, Eagle",
        color="#DC143C",
        image_file="romulus.png"
    ),
}


def get_gods_by_culture(culture: Culture) -> list[God]:
    """Get all gods from a specific culture."""
    return [god for god in GODS_DATABASE.values() if god.culture == culture]


def get_gods_by_archetype(archetype: Archetype) -> list[God]:
    """Get all gods matching a specific archetype."""
    return [god for god in GODS_DATABASE.values() if god.archetype == archetype]


def get_gods_by_gender(gender: str) -> list[God]:
    """Get all gods of a specific gender."""
    return [god for god in GODS_DATABASE.values() if god.gender == gender]


def get_god_by_id(god_id: str) -> God | None:
    """Get a god by their ID."""
    return GODS_DATABASE.get(god_id)


# Culture to region mapping for language-based filtering
CULTURE_REGION_MAP = {
    "korea": [Culture.KOREAN, Culture.CHINESE, Culture.JAPANESE, Culture.BUDDHIST, Culture.CONFUCIAN],
    "western": [Culture.GREEK, Culture.ROMAN, Culture.NORSE, Culture.CELTIC, Culture.CHRISTIAN, Culture.ARTHURIAN],
    "china": [Culture.CHINESE, Culture.JAPANESE, Culture.KOREAN, Culture.BUDDHIST, Culture.CONFUCIAN, Culture.TAOIST],
    "japan": [Culture.JAPANESE, Culture.CHINESE, Culture.BUDDHIST],
    "india": [Culture.HINDU, Culture.BUDDHIST],
    "middle_east": [Culture.MESOPOTAMIAN, Culture.ARABIC, Culture.EGYPTIAN, Culture.ISLAMIC, Culture.PERSIAN],
    "slavic": [Culture.SLAVIC, Culture.NORSE, Culture.CHRISTIAN],
    "southeast_asia": [Culture.THAI, Culture.VIETNAMESE, Culture.INDONESIAN, Culture.HINDU, Culture.BUDDHIST],
    "africa": [Culture.AFRICAN, Culture.EGYPTIAN],
    "americas": [Culture.AZTEC, Culture.MAYAN, Culture.NATIVE_AMERICAN],
    "oceania": [Culture.POLYNESIAN],
}


def get_gods_for_region(region: str) -> list[God]:
    """Get gods relevant to a specific region/language."""
    cultures = CULTURE_REGION_MAP.get(region, list(Culture))
    return [god for god in GODS_DATABASE.values() if god.culture in cultures]
