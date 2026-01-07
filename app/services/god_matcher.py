"""
God Matching Service
Matches facial features to mythological figures
"""
from dataclasses import dataclass
from typing import Optional
import random

from app.models.gods import (
    God, GODS_DATABASE, Culture, FaceShape, EyeType, Archetype,
    get_gods_by_culture, get_gods_for_region, CULTURE_REGION_MAP
)
from app.services.face_analysis import FaceFeatures


@dataclass
class MatchResult:
    """Result of god matching."""
    god: God
    match_score: float  # 0-1, how well the face matches
    face_shape_match: float
    eye_type_match: float
    symmetry_match: float
    intensity_match: float
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

        Args:
            features: Extracted facial features
            top_n: Number of top matches to return

        Returns:
            List of MatchResult objects, sorted by match score
        """
        results = []

        face_shape_enum = self.FACE_SHAPE_MAP.get(features.face_shape, FaceShape.OVAL)
        eye_type_enum = self.EYE_TYPE_MAP.get(features.eye_type, EyeType.SOFT)

        for god in self.available_gods:
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

            # Calculate overall match score with weights
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
                symmetry_match, intensity_match
            )

            results.append(MatchResult(
                god=god,
                match_score=min(1.0, match_score),
                face_shape_match=face_shape_match,
                eye_type_match=eye_type_match,
                symmetry_match=symmetry_match,
                intensity_match=intensity_match,
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

    def _generate_reasoning(
        self, features: FaceFeatures, god: God,
        face_match: float, eye_match: float,
        symmetry_match: float, intensity_match: float
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
