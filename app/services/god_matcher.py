"""
God Matching Service
Matches facial features to mythological figures
관상학(Physiognomy) 기반 매칭 로직 포함
"""
from dataclasses import dataclass
from typing import Optional
import random

from app.models.gods import (
    God, GODS_DATABASE, Culture, FaceShape, EyeType, Archetype,
    get_gods_by_culture, get_gods_for_region, CULTURE_REGION_MAP,
    FortuneType, EyeShapeType, PhysiognomyPreference
)
from app.services.face_analysis import FaceFeatures, PhysiognomyTraits


@dataclass
class MatchResult:
    """Result of god matching."""
    god: God
    match_score: float  # 0-1, how well the face matches
    face_shape_match: float
    eye_type_match: float
    symmetry_match: float
    intensity_match: float
    physiognomy_match: float  # 관상학 매칭 점수
    reasoning: str  # Explanation of why this god was matched


class GodMatcher:
    """Matches facial features to mythological figures."""

    # Mapping from string to enum
    FACE_SHAPE_MAP = {
        "oval": FaceShape.OVAL,
        "round": FaceShape.ROUND,
        "square": FaceShape.SQUARE,
        "heart": FaceShape.HEART,
        "oblong": FaceShape.OBLONG,
        "diamond": FaceShape.DIAMOND,
    }

    EYE_TYPE_MAP = {
        "sharp": EyeType.SHARP,
        "soft": EyeType.SOFT,
        "wide": EyeType.WIDE,
        "narrow": EyeType.NARROW,
        "deep": EyeType.DEEP,
        "bright": EyeType.BRIGHT,
    }

    # 관상학 눈 형태 매핑
    EYE_SHAPE_MAP = {
        "phoenix": EyeShapeType.PHOENIX,
        "tiger": EyeShapeType.TIGER,
        "deer": EyeShapeType.DEER,
        "dragon": EyeShapeType.DRAGON,
    }

    # 관상학 운세 유형 매핑
    FORTUNE_TYPE_MAP = {
        "leader": FortuneType.LEADER,
        "scholar": FortuneType.SCHOLAR,
        "warrior": FortuneType.WARRIOR,
        "artist": FortuneType.ARTIST,
        "merchant": FortuneType.MERCHANT,
    }

    def __init__(self, region: Optional[str] = None):
        """
        Initialize the god matcher.

        Args:
            region: Optional region to filter gods by (e.g., "korea", "western")
        """
        self.region = region
        if region and region in CULTURE_REGION_MAP:
            self.available_gods = get_gods_for_region(region)
        else:
            self.available_gods = list(GODS_DATABASE.values())

    def match(self, features: FaceFeatures, top_n: int = 5) -> list[MatchResult]:
        """
        Match facial features to gods.
        관상학 기반 매칭 로직 포함.
        성별 기반 필터링 포함.

        Args:
            features: Extracted facial features
            top_n: Number of top matches to return

        Returns:
            List of MatchResult objects, sorted by match score
        """
        results = []

        face_shape_enum = self.FACE_SHAPE_MAP.get(features.face_shape, FaceShape.OVAL)
        eye_type_enum = self.EYE_TYPE_MAP.get(features.eye_type, EyeType.SOFT)

        # Filter gods by detected gender if confidence is high enough
        detected_gender = getattr(features, 'gender', 'neutral')
        gender_confidence = getattr(features, 'gender_confidence', 0.5)

        # Only filter by gender if confidence > 0.6
        if gender_confidence > 0.6 and detected_gender in ['male', 'female']:
            gods_to_match = [
                god for god in self.available_gods
                if god.gender == detected_gender or god.gender == 'neutral'
            ]
            # Fallback if too few gods match
            if len(gods_to_match) < 10:
                gods_to_match = self.available_gods
        else:
            gods_to_match = self.available_gods

        for god in gods_to_match:
            # Calculate face shape match
            face_shape_match = self._calculate_face_shape_match(
                face_shape_enum, god.preferred_face_shapes
            )

            # Calculate eye type match
            eye_type_match = self._calculate_eye_type_match(
                eye_type_enum, god.preferred_eye_types
            )

            # Calculate symmetry match
            symmetry_match = self._calculate_symmetry_match(
                features.symmetry_score, god.symmetry_preference
            )

            # Calculate intensity match
            intensity_match = self._calculate_intensity_match(
                features.intensity_level, god.intensity_level
            )

            # 관상학 매칭 점수 계산
            physiognomy_match = self._calculate_physiognomy_match(
                features.physiognomy, god
            )

            # Calculate overall match score with weights
            # 관상학이 있으면 가중치 조정
            if features.physiognomy and god.physiognomy_pref:
                # 관상학 데이터가 있는 경우: 관상학 30% 반영
                match_score = (
                    face_shape_match * 0.18 +
                    eye_type_match * 0.18 +
                    symmetry_match * 0.14 +
                    intensity_match * 0.20 +
                    physiognomy_match * 0.30
                )
            else:
                # 기존 로직 유지
                match_score = (
                    face_shape_match * 0.25 +
                    eye_type_match * 0.25 +
                    symmetry_match * 0.2 +
                    intensity_match * 0.3
                )

            # Add small random factor to break ties
            match_score += random.uniform(0, 0.05)

            # Generate reasoning
            reasoning = self._generate_reasoning(
                features, god, face_shape_match, eye_type_match,
                symmetry_match, intensity_match, physiognomy_match
            )

            results.append(MatchResult(
                god=god,
                match_score=min(1.0, match_score),
                face_shape_match=face_shape_match,
                eye_type_match=eye_type_match,
                symmetry_match=symmetry_match,
                intensity_match=intensity_match,
                physiognomy_match=physiognomy_match,
                reasoning=reasoning
            ))

        # Sort by match score descending
        results.sort(key=lambda x: x.match_score, reverse=True)

        return results[:top_n]

    def match_single(self, features: FaceFeatures) -> MatchResult:
        """Get the single best matching god."""
        results = self.match(features, top_n=1)
        return results[0] if results else None

    def _calculate_face_shape_match(
        self, user_shape: FaceShape, god_shapes: list[FaceShape]
    ) -> float:
        """Calculate how well user's face shape matches god's preferences."""
        if user_shape in god_shapes:
            # Direct match - higher if it's the primary preference
            idx = god_shapes.index(user_shape)
            return 1.0 - (idx * 0.1)

        # No direct match - calculate similarity
        shape_similarity = {
            FaceShape.OVAL: [FaceShape.OBLONG, FaceShape.HEART, FaceShape.ROUND],
            FaceShape.ROUND: [FaceShape.OVAL, FaceShape.SQUARE],
            FaceShape.SQUARE: [FaceShape.ROUND, FaceShape.OBLONG, FaceShape.DIAMOND],
            FaceShape.HEART: [FaceShape.OVAL, FaceShape.DIAMOND],
            FaceShape.OBLONG: [FaceShape.OVAL, FaceShape.SQUARE],
            FaceShape.DIAMOND: [FaceShape.HEART, FaceShape.OVAL, FaceShape.SQUARE],
        }

        similar_shapes = shape_similarity.get(user_shape, [])
        for similar in similar_shapes:
            if similar in god_shapes:
                return 0.6

        return 0.3

    def _calculate_eye_type_match(
        self, user_type: EyeType, god_types: list[EyeType]
    ) -> float:
        """Calculate how well user's eye type matches god's preferences."""
        if user_type in god_types:
            idx = god_types.index(user_type)
            return 1.0 - (idx * 0.1)

        # Eye type similarity
        type_similarity = {
            EyeType.SHARP: [EyeType.NARROW, EyeType.DEEP],
            EyeType.SOFT: [EyeType.WIDE, EyeType.BRIGHT],
            EyeType.WIDE: [EyeType.SOFT, EyeType.BRIGHT],
            EyeType.NARROW: [EyeType.SHARP, EyeType.DEEP],
            EyeType.DEEP: [EyeType.SHARP, EyeType.NARROW],
            EyeType.BRIGHT: [EyeType.WIDE, EyeType.SOFT],
        }

        similar_types = type_similarity.get(user_type, [])
        for similar in similar_types:
            if similar in god_types:
                return 0.6

        return 0.3

    def _calculate_symmetry_match(
        self, user_symmetry: float, god_preference: float
    ) -> float:
        """Calculate symmetry match score."""
        # Calculate how close user's symmetry is to god's preference
        diff = abs(user_symmetry - god_preference)

        # High symmetry users match well with gods who prefer high symmetry
        # But gods with low symmetry preference (like Loki) match better with asymmetric faces
        if god_preference > 0.85:
            # Gods preferring high symmetry
            return max(0.0, 1.0 - diff * 2)
        else:
            # Gods okay with some asymmetry
            return max(0.0, 1.0 - diff)

    def _calculate_intensity_match(
        self, user_intensity: float, god_intensity: float
    ) -> float:
        """Calculate intensity level match."""
        diff = abs(user_intensity - god_intensity)
        return max(0.0, 1.0 - diff)

    def _calculate_physiognomy_match(
        self, user_physiognomy: Optional[PhysiognomyTraits], god: God
    ) -> float:
        """
        관상학 기반 매칭 점수 계산.

        Args:
            user_physiognomy: 사용자의 관상학 분석 결과
            god: 신화 캐릭터

        Returns:
            0-1 범위의 매칭 점수
        """
        if not user_physiognomy:
            return 0.5  # 관상학 데이터 없으면 중립 점수

        # 캐릭터에 관상학 선호도가 없으면 아키타입 기반으로 자동 생성
        god_pref = god.physiognomy_pref or self._generate_default_physiognomy_pref(god)

        total_score = 0.0
        weights = 0.0

        # 1. 종합 관상 유형 매칭 (가장 중요)
        fortune_enum = self.FORTUNE_TYPE_MAP.get(user_physiognomy.overall_fortune)
        if fortune_enum and fortune_enum in god_pref.preferred_fortunes:
            idx = god_pref.preferred_fortunes.index(fortune_enum)
            total_score += (1.0 - idx * 0.2) * 0.30
        else:
            total_score += 0.3 * 0.30
        weights += 0.30

        # 2. 눈 형태 매칭
        eye_shape_enum = self.EYE_SHAPE_MAP.get(user_physiognomy.eye_shape)
        if eye_shape_enum and eye_shape_enum in god_pref.preferred_eye_shapes:
            idx = god_pref.preferred_eye_shapes.index(eye_shape_enum)
            total_score += (1.0 - idx * 0.15) * 0.15
        else:
            total_score += 0.4 * 0.15
        weights += 0.15

        # 3. 이마 점수 매칭
        forehead_diff = abs(user_physiognomy.forehead_score - god_pref.forehead_preference)
        total_score += max(0.0, 1.0 - forehead_diff) * 0.12
        weights += 0.12

        # 4. 코 점수 매칭
        nose_diff = abs(user_physiognomy.nose_bridge_score - god_pref.nose_preference)
        total_score += max(0.0, 1.0 - nose_diff) * 0.12
        weights += 0.12

        # 5. 턱 강도 매칭
        jaw_diff = abs(user_physiognomy.jaw_strength - god_pref.jaw_preference)
        total_score += max(0.0, 1.0 - jaw_diff) * 0.12
        weights += 0.12

        # 6. 광대뼈 매칭
        cheek_diff = abs(user_physiognomy.cheekbone_prominence - god_pref.cheekbone_preference)
        total_score += max(0.0, 1.0 - cheek_diff) * 0.10
        weights += 0.10

        # 7. 눈의 정기 매칭
        spirit_diff = abs(user_physiognomy.eye_spirit - god_pref.eye_spirit_preference)
        total_score += max(0.0, 1.0 - spirit_diff) * 0.09
        weights += 0.09

        return total_score / weights if weights > 0 else 0.5

    def _generate_default_physiognomy_pref(self, god: God) -> PhysiognomyPreference:
        """
        아키타입과 캐릭터 특성 기반으로 기본 관상학 선호도 생성.
        """
        # 아키타입별 기본 관상 유형 매핑
        archetype_fortunes = {
            Archetype.RULER: [FortuneType.LEADER, FortuneType.WARRIOR],
            Archetype.SAGE: [FortuneType.SCHOLAR, FortuneType.ARTIST],
            Archetype.HERO: [FortuneType.WARRIOR, FortuneType.LEADER],
            Archetype.REBEL: [FortuneType.WARRIOR, FortuneType.ARTIST],
            Archetype.WIZARD: [FortuneType.SCHOLAR, FortuneType.ARTIST],
            Archetype.LOVER: [FortuneType.ARTIST, FortuneType.MERCHANT],
            Archetype.JESTER: [FortuneType.ARTIST, FortuneType.MERCHANT],
            Archetype.CAREGIVER: [FortuneType.SCHOLAR, FortuneType.LEADER],
            Archetype.CREATOR: [FortuneType.ARTIST, FortuneType.SCHOLAR],
            Archetype.INNOCENT: [FortuneType.ARTIST, FortuneType.SCHOLAR],
            Archetype.EXPLORER: [FortuneType.WARRIOR, FortuneType.MERCHANT],
            Archetype.EVERYMAN: [FortuneType.MERCHANT, FortuneType.SCHOLAR],
        }

        # 아키타입별 눈 형태 매핑
        archetype_eye_shapes = {
            Archetype.RULER: [EyeShapeType.DRAGON, EyeShapeType.TIGER],
            Archetype.SAGE: [EyeShapeType.PHOENIX, EyeShapeType.DRAGON],
            Archetype.HERO: [EyeShapeType.TIGER, EyeShapeType.DRAGON],
            Archetype.REBEL: [EyeShapeType.TIGER, EyeShapeType.PHOENIX],
            Archetype.WIZARD: [EyeShapeType.DRAGON, EyeShapeType.PHOENIX],
            Archetype.LOVER: [EyeShapeType.DEER, EyeShapeType.PHOENIX],
            Archetype.JESTER: [EyeShapeType.DEER, EyeShapeType.PHOENIX],
            Archetype.CAREGIVER: [EyeShapeType.DEER, EyeShapeType.PHOENIX],
            Archetype.CREATOR: [EyeShapeType.PHOENIX, EyeShapeType.DEER],
            Archetype.INNOCENT: [EyeShapeType.DEER, EyeShapeType.PHOENIX],
            Archetype.EXPLORER: [EyeShapeType.TIGER, EyeShapeType.PHOENIX],
            Archetype.EVERYMAN: [EyeShapeType.DEER, EyeShapeType.DRAGON],
        }

        fortunes = archetype_fortunes.get(god.archetype, [FortuneType.SCHOLAR])
        eye_shapes = archetype_eye_shapes.get(god.archetype, [EyeShapeType.DRAGON])

        # 강렬도에 따른 특징 선호도 조정
        intensity = god.intensity_level

        return PhysiognomyPreference(
            preferred_fortunes=fortunes,
            preferred_eye_shapes=eye_shapes,
            forehead_preference=0.7 if god.archetype in [Archetype.SAGE, Archetype.RULER] else 0.6,
            nose_preference=intensity * 0.8 + 0.2,
            jaw_preference=intensity * 0.6 + 0.3,
            cheekbone_preference=0.7 if god.archetype in [Archetype.RULER, Archetype.HERO] else 0.5,
            eye_spirit_preference=intensity * 0.5 + 0.4
        )

    def _generate_reasoning(
        self, features: FaceFeatures, god: God,
        face_match: float, eye_match: float,
        symmetry_match: float, intensity_match: float,
        physiognomy_match: float = 0.5
    ) -> str:
        """Generate explanation for the match."""
        reasons = []

        # Face shape
        if face_match > 0.8:
            reasons.append(f"Your {features.face_shape} face shape perfectly aligns with {god.id.replace('_', ' ').title()}'s aesthetic")
        elif face_match > 0.5:
            reasons.append(f"Your facial structure resonates with {god.id.replace('_', ' ').title()}'s essence")

        # Eye type
        if eye_match > 0.8:
            reasons.append(f"Your {features.eye_type} eyes reflect the gaze of {god.domain.split(',')[0].strip()}")
        elif eye_match > 0.5:
            reasons.append(f"Your eyes carry the wisdom befitting a divine being")

        # Symmetry
        if symmetry_match > 0.8:
            if god.symmetry_preference > 0.85:
                reasons.append("The harmony of your features mirrors divine perfection")
            else:
                reasons.append("Your unique features embody the unpredictable nature of this deity")

        # Intensity
        if intensity_match > 0.8:
            if god.intensity_level > 0.7:
                reasons.append("Your commanding presence matches this powerful figure")
            else:
                reasons.append("Your gentle aura reflects this deity's serene nature")

        # 관상학 기반 reasoning (Physiognomy-based reasoning)
        if physiognomy_match > 0.7 and features.physiognomy:
            fortune_descriptions = {
                "leader": "leadership destiny written in your features",
                "scholar": "wisdom reflected in your countenance",
                "warrior": "warrior spirit in your expression",
                "artist": "creative soul visible in your features",
                "merchant": "prosperity marked in your face",
            }
            eye_shape_descriptions = {
                "phoenix": "phoenix eyes that see beyond the ordinary",
                "tiger": "tiger eyes filled with determination",
                "deer": "gentle deer eyes radiating warmth",
                "dragon": "dragon eyes commanding respect",
            }

            if features.physiognomy.overall_fortune in fortune_descriptions:
                reasons.append(f"Your face reveals {fortune_descriptions[features.physiognomy.overall_fortune]}")
            if features.physiognomy.eye_shape in eye_shape_descriptions:
                reasons.append(f"You have {eye_shape_descriptions[features.physiognomy.eye_shape]}")

        # Archetype reasoning
        archetype_traits = {
            Archetype.RULER: "natural leadership qualities",
            Archetype.SAGE: "wisdom in your expression",
            Archetype.HERO: "courage reflected in your features",
            Archetype.REBEL: "independent spirit",
            Archetype.WIZARD: "mysterious depth",
            Archetype.LOVER: "grace and beauty",
            Archetype.JESTER: "playful energy",
            Archetype.CAREGIVER: "nurturing warmth",
            Archetype.CREATOR: "creative vision",
            Archetype.INNOCENT: "pure radiance",
            Archetype.EXPLORER: "adventurous spirit",
            Archetype.EVERYMAN: "relatable authenticity",
        }

        trait = archetype_traits.get(god.archetype, "unique essence")
        reasons.append(f"You possess {trait}")

        return ". ".join(reasons) + "."


def match_face_to_god(
    features: FaceFeatures,
    region: Optional[str] = None,
    top_n: int = 5
) -> list[MatchResult]:
    """
    Convenience function to match facial features to gods.

    Args:
        features: Extracted facial features
        region: Optional region filter
        top_n: Number of matches to return

    Returns:
        List of match results
    """
    matcher = GodMatcher(region=region)
    return matcher.match(features, top_n=top_n)


def get_primary_match(
    features: FaceFeatures,
    region: Optional[str] = None
) -> MatchResult:
    """Get the single best matching god."""
    matcher = GodMatcher(region=region)
    return matcher.match_single(features)
