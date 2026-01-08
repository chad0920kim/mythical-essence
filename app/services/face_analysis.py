"""
Face Analysis Service
Analyzes facial features using MediaPipe for matching with mythological figures
"""
import cv2
import numpy as np
from dataclasses import dataclass
from typing import Optional
from pathlib import Path

MEDIAPIPE_AVAILABLE = False
mp = None

try:
    import mediapipe as mp
    # Test that solutions actually work
    if hasattr(mp, 'solutions') and hasattr(mp.solutions, 'face_mesh'):
        MEDIAPIPE_AVAILABLE = True
except (ImportError, AttributeError, Exception) as e:
    print(f"MediaPipe not available: {e}")
    MEDIAPIPE_AVAILABLE = False


@dataclass
class PhysiognomyTraits:
    """관상학(Physiognomy) 기반 얼굴 특성 분석."""
    # 이마 (額 - Forehead): 지혜, 초년운
    forehead_type: str       # "wide" (넓음), "narrow" (좁음), "high" (높음), "rounded" (둥근)
    forehead_score: float    # 0-1, 이마의 발달 정도

    # 눈썹 (眉 - Eyebrows): 성격, 형제운
    eyebrow_type: str        # "thick" (짙음), "thin" (옅음), "arched" (아치형), "straight" (일자)
    eyebrow_distance: float  # 0-1, 눈썹 간격 (좁으면 결단력, 넓으면 관대함)

    # 눈 (目 - Eyes): 정신력, 중년운
    eye_spirit: float        # 0-1, 눈의 정기/광채 (높을수록 강한 정신력)
    eye_shape: str           # "phoenix" (봉황눈), "tiger" (호랑이눈), "deer" (사슴눈), "dragon" (용눈)

    # 코 (鼻 - Nose): 재물운, 자존심
    nose_type: str           # "high" (높음), "flat" (낮음), "aquiline" (매부리), "straight" (곧음)
    nose_bridge_score: float # 0-1, 콧대 높이

    # 광대뼈 (顴 - Cheekbones): 권력, 사회성
    cheekbone_prominence: float  # 0-1, 광대뼈 돌출 정도

    # 턱 (頷 - Chin/Jaw): 의지력, 말년운
    jaw_type: str            # "strong" (강함), "soft" (부드러움), "square" (각짐), "pointed" (뾰족함)
    jaw_strength: float      # 0-1, 턱의 발달 정도

    # 입 (口 - Mouth): 표현력, 식복
    mouth_type: str          # "wide" (넓음), "small" (작음), "full" (도톰), "thin" (얇음)

    # 인중 (人中 - Philtrum): 수명, 자녀운
    philtrum_depth: float    # 0-1, 인중 깊이

    # 종합 관상 분류
    overall_fortune: str     # "leader" (리더상), "scholar" (학자상), "warrior" (무관상), "artist" (예술가상), "merchant" (상인상)


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

    # 관상학 특성 (Physiognomy traits)
    physiognomy: Optional[PhysiognomyTraits] = None


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
            'left_brow_top': 105,
            'right_brow_inner': 336,
            'right_brow_outer': 300,
            'right_brow_top': 334,

            # Nose (관상학 - 코)
            'nose_tip': 1,
            'nose_bridge': 6,
            'nose_bridge_top': 168,
            'nose_left': 129,
            'nose_right': 358,

            # Mouth (관상학 - 입)
            'mouth_left': 61,
            'mouth_right': 291,
            'mouth_top': 13,
            'mouth_bottom': 14,
            'upper_lip_top': 0,
            'lower_lip_bottom': 17,

            # Philtrum (관상학 - 인중)
            'philtrum_top': 164,
            'philtrum_bottom': 18,

            # Cheekbones (관상학 - 광대뼈)
            'left_cheekbone': 116,
            'right_cheekbone': 345,

            # Forehead additional points
            'forehead_left': 67,
            'forehead_right': 297,
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

        # 관상학(Physiognomy) 분석
        physiognomy = self._analyze_physiognomy(
            points, face_width, face_height, forehead_ratio,
            jaw_width_ratio, eye_size_ratio, eye_angle, brow_height, mouth_width_ratio
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
            intensity_level=intensity_level,
            physiognomy=physiognomy
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

    def _analyze_physiognomy(
        self, points: dict, face_width: float, face_height: float,
        forehead_ratio: float, jaw_width_ratio: float,
        eye_size_ratio: float, eye_angle: float,
        brow_height: float, mouth_width_ratio: float
    ) -> PhysiognomyTraits:
        """관상학 기반 얼굴 특성 분석."""

        # 1. 이마 분석 (額)
        forehead_width = self._distance(points['forehead_left'], points['forehead_right'])
        forehead_width_ratio = forehead_width / face_width if face_width > 0 else 0.8

        if forehead_ratio > 0.36:
            forehead_type = "high"
        elif forehead_ratio < 0.30:
            forehead_type = "low"
        elif forehead_width_ratio > 0.85:
            forehead_type = "wide"
        else:
            forehead_type = "rounded"
        forehead_score = min(1.0, forehead_ratio * 2.5)

        # 2. 눈썹 분석 (眉)
        left_brow_width = self._distance(points['left_brow_inner'], points['left_brow_outer'])
        left_brow_height = self._distance(points['left_brow_inner'], points['left_brow_top'])
        brow_thickness = left_brow_height / left_brow_width if left_brow_width > 0 else 0.2

        if brow_thickness > 0.25:
            eyebrow_type = "thick"
        elif brow_thickness < 0.15:
            eyebrow_type = "thin"
        elif brow_height > 0.06:
            eyebrow_type = "arched"
        else:
            eyebrow_type = "straight"

        brow_gap = self._distance(points['left_brow_inner'], points['right_brow_inner'])
        eyebrow_distance = brow_gap / face_width if face_width > 0 else 0.15

        # 3. 눈 분석 (目) - 관상학적 눈 형태
        eye_spirit = min(1.0, (eye_size_ratio * 2) + (eye_angle * 0.5))

        if eye_angle > 0.6 and eye_size_ratio > 0.26:
            eye_shape = "phoenix"  # 봉황눈 - 크고 날카로운
        elif eye_angle < 0.4 and jaw_width_ratio > 0.8:
            eye_shape = "tiger"    # 호랑이눈 - 날카롭고 강인한
        elif eye_size_ratio > 0.28 and eye_angle > 0.5:
            eye_shape = "deer"     # 사슴눈 - 크고 순한
        else:
            eye_shape = "dragon"   # 용눈 - 깊고 위엄있는

        # 4. 코 분석 (鼻)
        nose_height = self._distance(points['nose_bridge_top'], points['nose_tip'])
        nose_width = self._distance(points['nose_left'], points['nose_right'])
        nose_ratio = nose_height / nose_width if nose_width > 0 else 1.5
        nose_bridge_score = min(1.0, nose_ratio / 2)

        if nose_ratio > 1.8:
            nose_type = "high"
        elif nose_ratio < 1.2:
            nose_type = "flat"
        elif nose_bridge_score > 0.7:
            nose_type = "aquiline"
        else:
            nose_type = "straight"

        # 5. 광대뼈 분석 (顴)
        cheekbone_width = self._distance(points['left_cheekbone'], points['right_cheekbone'])
        cheekbone_prominence = cheekbone_width / face_width if face_width > 0 else 0.7

        # 6. 턱 분석 (頷)
        if jaw_width_ratio > 0.85:
            jaw_type = "square"
        elif jaw_width_ratio > 0.78:
            jaw_type = "strong"
        elif jaw_width_ratio < 0.7:
            jaw_type = "pointed"
        else:
            jaw_type = "soft"
        jaw_strength = jaw_width_ratio

        # 7. 입 분석 (口)
        lip_height = self._distance(points['upper_lip_top'], points['lower_lip_bottom'])
        lip_ratio = lip_height / face_height if face_height > 0 else 0.1

        if mouth_width_ratio > 0.45:
            mouth_type = "wide"
        elif mouth_width_ratio < 0.35:
            mouth_type = "small"
        elif lip_ratio > 0.12:
            mouth_type = "full"
        else:
            mouth_type = "thin"

        # 8. 인중 분석 (人中)
        philtrum_length = self._distance(points['philtrum_top'], points['philtrum_bottom'])
        philtrum_depth = philtrum_length / face_height if face_height > 0 else 0.05

        # 9. 종합 관상 분류
        overall_fortune = self._classify_fortune(
            forehead_score, eye_spirit, nose_bridge_score,
            jaw_strength, cheekbone_prominence
        )

        return PhysiognomyTraits(
            forehead_type=forehead_type,
            forehead_score=forehead_score,
            eyebrow_type=eyebrow_type,
            eyebrow_distance=eyebrow_distance,
            eye_spirit=eye_spirit,
            eye_shape=eye_shape,
            nose_type=nose_type,
            nose_bridge_score=nose_bridge_score,
            cheekbone_prominence=cheekbone_prominence,
            jaw_type=jaw_type,
            jaw_strength=jaw_strength,
            mouth_type=mouth_type,
            philtrum_depth=philtrum_depth,
            overall_fortune=overall_fortune
        )

    def _classify_fortune(
        self, forehead: float, eye_spirit: float, nose: float,
        jaw: float, cheekbone: float
    ) -> str:
        """종합 관상 분류 - 리더상, 학자상, 무관상, 예술가상, 상인상."""
        scores = {
            "leader": forehead * 0.3 + jaw * 0.3 + cheekbone * 0.2 + eye_spirit * 0.2,
            "scholar": forehead * 0.4 + eye_spirit * 0.3 + nose * 0.2 + jaw * 0.1,
            "warrior": jaw * 0.35 + cheekbone * 0.25 + eye_spirit * 0.25 + nose * 0.15,
            "artist": eye_spirit * 0.35 + forehead * 0.25 + nose * 0.2 + cheekbone * 0.2,
            "merchant": nose * 0.3 + cheekbone * 0.25 + jaw * 0.25 + forehead * 0.2,
        }
        return max(scores, key=scores.get)

    def _generate_mock_features(self) -> FaceFeatures:
        """Generate mock features for testing without MediaPipe."""
        import random

        shapes = ["oval", "round", "square", "heart", "oblong", "diamond"]
        eye_types = ["sharp", "soft", "wide", "narrow", "deep", "bright"]
        forehead_types = ["wide", "narrow", "high", "rounded"]
        eyebrow_types = ["thick", "thin", "arched", "straight"]
        eye_shapes = ["phoenix", "tiger", "deer", "dragon"]
        nose_types = ["high", "flat", "aquiline", "straight"]
        jaw_types = ["strong", "soft", "square", "pointed"]
        mouth_types = ["wide", "small", "full", "thin"]
        fortunes = ["leader", "scholar", "warrior", "artist", "merchant"]

        # Generate mock physiognomy
        mock_physiognomy = PhysiognomyTraits(
            forehead_type=random.choice(forehead_types),
            forehead_score=random.uniform(0.6, 0.95),
            eyebrow_type=random.choice(eyebrow_types),
            eyebrow_distance=random.uniform(0.12, 0.20),
            eye_spirit=random.uniform(0.5, 0.95),
            eye_shape=random.choice(eye_shapes),
            nose_type=random.choice(nose_types),
            nose_bridge_score=random.uniform(0.5, 0.9),
            cheekbone_prominence=random.uniform(0.6, 0.85),
            jaw_type=random.choice(jaw_types),
            jaw_strength=random.uniform(0.7, 0.9),
            mouth_type=random.choice(mouth_types),
            philtrum_depth=random.uniform(0.04, 0.08),
            overall_fortune=random.choice(fortunes)
        )

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
            intensity_level=random.uniform(0.3, 0.9),
            physiognomy=mock_physiognomy
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
