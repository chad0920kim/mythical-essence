"""
Face Analysis Service
Analyzes facial features using MediaPipe for matching with mythological figures
"""
import cv2
import numpy as np
from dataclasses import dataclass
from typing import Optional
from pathlib import Path

try:
    import mediapipe as mp
    MEDIAPIPE_AVAILABLE = True
except ImportError:
    MEDIAPIPE_AVAILABLE = False


@dataclass
class FaceFeatures:
    """Extracted facial features for god matching."""
    # Face shape indicators
    face_width_ratio: float  # Width to height ratio
    jaw_width_ratio: float   # Jaw width relative to face width
    forehead_ratio: float    # Forehead height ratio

    # Eye features
    eye_size_ratio: float    # Eye size relative to face
    eye_distance_ratio: float  # Distance between eyes
    eye_angle: float         # Angle of eye corners (sharp vs soft)

    # Symmetry
    symmetry_score: float    # 0-1, how symmetric the face is

    # Intensity/Expression
    brow_height: float       # Eyebrow position
    mouth_width_ratio: float # Mouth width relative to face

    # Overall classification
    face_shape: str          # oval, round, square, heart, oblong, diamond
    eye_type: str            # sharp, soft, wide, narrow, deep, bright
    intensity_level: float   # 0-1, soft to intense features


class FaceAnalyzer:
    """Analyzes facial features using MediaPipe Face Mesh."""

    def __init__(self):
        if not MEDIAPIPE_AVAILABLE:
            self.face_mesh = None
            return

        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )

        # Key landmark indices for face analysis
        # https://github.com/google/mediapipe/blob/master/mediapipe/modules/face_geometry/data/canonical_face_model_uv_visualization.png
        self.landmarks = {
            # Face contour
            'chin': 152,
            'left_cheek': 234,
            'right_cheek': 454,
            'forehead_top': 10,
            'left_jaw': 172,
            'right_jaw': 397,

            # Eyes
            'left_eye_inner': 133,
            'left_eye_outer': 33,
            'left_eye_top': 159,
            'left_eye_bottom': 145,
            'right_eye_inner': 362,
            'right_eye_outer': 263,
            'right_eye_top': 386,
            'right_eye_bottom': 374,

            # Eyebrows
            'left_brow_inner': 107,
            'left_brow_outer': 70,
            'right_brow_inner': 336,
            'right_brow_outer': 300,

            # Nose
            'nose_tip': 1,
            'nose_bridge': 6,

            # Mouth
            'mouth_left': 61,
            'mouth_right': 291,
            'mouth_top': 13,
            'mouth_bottom': 14,
        }

    def analyze(self, image: np.ndarray) -> Optional[FaceFeatures]:
        """
        Analyze facial features from an image.

        Args:
            image: BGR image as numpy array

        Returns:
            FaceFeatures object or None if no face detected
        """
        if not MEDIAPIPE_AVAILABLE or self.face_mesh is None:
            # Return mock data for testing without MediaPipe
            return self._generate_mock_features()

        # Convert BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process image
        results = self.face_mesh.process(rgb_image)

        if not results.multi_face_landmarks:
            return None

        # Get first face
        face_landmarks = results.multi_face_landmarks[0]
        h, w = image.shape[:2]

        # Convert landmarks to pixel coordinates
        points = {}
        for name, idx in self.landmarks.items():
            lm = face_landmarks.landmark[idx]
            points[name] = (lm.x * w, lm.y * h)

        # Calculate face dimensions
        face_width = self._distance(points['left_cheek'], points['right_cheek'])
        face_height = self._distance(points['forehead_top'], points['chin'])
        jaw_width = self._distance(points['left_jaw'], points['right_jaw'])

        # Calculate face width ratio
        face_width_ratio = face_width / face_height if face_height > 0 else 1.0
        jaw_width_ratio = jaw_width / face_width if face_width > 0 else 1.0

        # Calculate forehead ratio
        forehead_height = self._distance(points['forehead_top'], points['nose_bridge'])
        forehead_ratio = forehead_height / face_height if face_height > 0 else 0.33

        # Calculate eye features
        left_eye_width = self._distance(points['left_eye_inner'], points['left_eye_outer'])
        right_eye_width = self._distance(points['right_eye_inner'], points['right_eye_outer'])
        avg_eye_width = (left_eye_width + right_eye_width) / 2
        eye_size_ratio = avg_eye_width / face_width if face_width > 0 else 0.25

        eye_distance = self._distance(points['left_eye_inner'], points['right_eye_inner'])
        eye_distance_ratio = eye_distance / face_width if face_width > 0 else 0.3

        # Calculate eye angle (sharpness)
        left_eye_angle = self._calculate_angle(
            points['left_eye_inner'], points['left_eye_outer'],
            points['left_eye_top'], points['left_eye_bottom']
        )
        eye_angle = left_eye_angle

        # Calculate symmetry
        left_side_features = [
            points['left_eye_inner'], points['left_eye_outer'],
            points['left_brow_inner'], points['left_brow_outer'],
            points['left_cheek']
        ]
        right_side_features = [
            points['right_eye_inner'], points['right_eye_outer'],
            points['right_brow_inner'], points['right_brow_outer'],
            points['right_cheek']
        ]
        symmetry_score = self._calculate_symmetry(left_side_features, right_side_features, points['nose_tip'][0])

        # Calculate brow height
        left_brow_dist = self._distance(points['left_brow_inner'], points['left_eye_top'])
        brow_height = left_brow_dist / face_height if face_height > 0 else 0.05

        # Calculate mouth width
        mouth_width = self._distance(points['mouth_left'], points['mouth_right'])
        mouth_width_ratio = mouth_width / face_width if face_width > 0 else 0.4

        # Classify face shape
        face_shape = self._classify_face_shape(
            face_width_ratio, jaw_width_ratio, forehead_ratio
        )

        # Classify eye type
        eye_type = self._classify_eye_type(
            eye_size_ratio, eye_angle, eye_distance_ratio
        )

        # Calculate intensity level
        intensity_level = self._calculate_intensity(
            jaw_width_ratio, eye_angle, brow_height
        )

        return FaceFeatures(
            face_width_ratio=face_width_ratio,
            jaw_width_ratio=jaw_width_ratio,
            forehead_ratio=forehead_ratio,
            eye_size_ratio=eye_size_ratio,
            eye_distance_ratio=eye_distance_ratio,
            eye_angle=eye_angle,
            symmetry_score=symmetry_score,
            brow_height=brow_height,
            mouth_width_ratio=mouth_width_ratio,
            face_shape=face_shape,
            eye_type=eye_type,
            intensity_level=intensity_level
        )

    def _distance(self, p1: tuple, p2: tuple) -> float:
        """Calculate Euclidean distance between two points."""
        return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def _calculate_angle(self, inner: tuple, outer: tuple, top: tuple, bottom: tuple) -> float:
        """Calculate eye opening angle (0-1, narrow to wide)."""
        width = self._distance(inner, outer)
        height = self._distance(top, bottom)
        if width == 0:
            return 0.5
        ratio = height / width
        # Normalize to 0-1 range (typical ratio is 0.3-0.5)
        return min(1.0, max(0.0, (ratio - 0.2) / 0.4))

    def _calculate_symmetry(self, left_features: list, right_features: list, center_x: float) -> float:
        """Calculate facial symmetry score."""
        if len(left_features) != len(right_features):
            return 0.5

        total_diff = 0
        for left, right in zip(left_features, right_features):
            left_dist = abs(left[0] - center_x)
            right_dist = abs(right[0] - center_x)
            if max(left_dist, right_dist) > 0:
                diff = abs(left_dist - right_dist) / max(left_dist, right_dist)
                total_diff += diff

        avg_diff = total_diff / len(left_features)
        return max(0.0, min(1.0, 1.0 - avg_diff))

    def _classify_face_shape(self, width_ratio: float, jaw_ratio: float, forehead_ratio: float) -> str:
        """Classify face shape based on measurements."""
        if width_ratio > 0.9:
            if jaw_ratio > 0.85:
                return "square"
            else:
                return "round"
        elif width_ratio < 0.7:
            if forehead_ratio > 0.35:
                return "oblong"
            else:
                return "oval"
        else:
            if jaw_ratio < 0.75:
                if forehead_ratio > 0.35:
                    return "heart"
                else:
                    return "diamond"
            else:
                return "oval"

    def _classify_eye_type(self, size_ratio: float, angle: float, distance_ratio: float) -> str:
        """Classify eye type based on measurements."""
        if size_ratio > 0.28:
            if angle > 0.6:
                return "wide"
            else:
                return "bright"
        elif size_ratio < 0.22:
            if angle < 0.4:
                return "narrow"
            else:
                return "deep"
        else:
            if angle > 0.5:
                return "soft"
            else:
                return "sharp"

    def _calculate_intensity(self, jaw_ratio: float, eye_angle: float, brow_height: float) -> float:
        """Calculate overall facial intensity (soft to intense)."""
        # Higher jaw ratio, lower eye angle, lower brow = more intense
        intensity = 0.0
        intensity += (jaw_ratio - 0.7) * 2  # Jaw contribution
        intensity += (1 - eye_angle) * 0.3  # Eye sharpness contribution
        intensity += (0.06 - brow_height) * 5  # Brow contribution

        return max(0.0, min(1.0, 0.5 + intensity))

    def _generate_mock_features(self) -> FaceFeatures:
        """Generate mock features for testing without MediaPipe."""
        import random

        shapes = ["oval", "round", "square", "heart", "oblong", "diamond"]
        eye_types = ["sharp", "soft", "wide", "narrow", "deep", "bright"]

        return FaceFeatures(
            face_width_ratio=random.uniform(0.7, 0.95),
            jaw_width_ratio=random.uniform(0.7, 0.9),
            forehead_ratio=random.uniform(0.28, 0.38),
            eye_size_ratio=random.uniform(0.2, 0.3),
            eye_distance_ratio=random.uniform(0.25, 0.35),
            eye_angle=random.uniform(0.3, 0.7),
            symmetry_score=random.uniform(0.7, 0.98),
            brow_height=random.uniform(0.04, 0.08),
            mouth_width_ratio=random.uniform(0.35, 0.5),
            face_shape=random.choice(shapes),
            eye_type=random.choice(eye_types),
            intensity_level=random.uniform(0.3, 0.9)
        )

    def analyze_from_file(self, image_path: str) -> Optional[FaceFeatures]:
        """Analyze facial features from an image file."""
        path = Path(image_path)
        if not path.exists():
            return None

        image = cv2.imread(str(path))
        if image is None:
            return None

        return self.analyze(image)

    def analyze_from_bytes(self, image_bytes: bytes) -> Optional[FaceFeatures]:
        """Analyze facial features from image bytes."""
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            return None

        return self.analyze(image)


# Singleton instance
_analyzer: Optional[FaceAnalyzer] = None


def get_face_analyzer() -> FaceAnalyzer:
    """Get or create the face analyzer singleton."""
    global _analyzer
    if _analyzer is None:
        _analyzer = FaceAnalyzer()
    return _analyzer
