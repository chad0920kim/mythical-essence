"""
Face Swap Service
Handles face swapping with pre-made god templates
"""
import cv2
import numpy as np
from pathlib import Path
from typing import Optional
from PIL import Image
import io

from app.config import GODS_IMAGES_DIR, OUTPUT_IMAGE_SIZE


class FaceSwapper:
    """
    Face swapping service using InsightFace.
    Falls back to overlay mode if InsightFace is not available.
    """

    def __init__(self):
        self.insightface_available = False
        self.swapper = None
        self.app = None

        try:
            import insightface
            from insightface.app import FaceAnalysis

            # Initialize InsightFace
            self.app = FaceAnalysis(name='buffalo_l')
            self.app.prepare(ctx_id=0, det_size=(640, 640))

            # Try to load swapper model
            model_path = Path.home() / '.insightface' / 'models' / 'inswapper_128.onnx'
            if model_path.exists():
                self.swapper = insightface.model_zoo.get_model(str(model_path))
                self.insightface_available = True
            else:
                print(f"InsightFace swapper model not found at {model_path}")
                print("Face swap will use overlay mode instead.")

        except ImportError:
            print("InsightFace not available. Using overlay mode.")
        except Exception as e:
            print(f"Error initializing InsightFace: {e}")
            print("Using overlay mode.")

    def swap_face(
        self,
        source_image: np.ndarray,
        target_god_id: str,
        output_size: tuple = OUTPUT_IMAGE_SIZE
    ) -> Optional[np.ndarray]:
        """
        Swap face from source image onto god template.

        Args:
            source_image: User's image (BGR numpy array)
            target_god_id: ID of the god template to use
            output_size: Output image dimensions

        Returns:
            Result image with swapped face, or None if failed
        """
        # Load god template
        template_path = GODS_IMAGES_DIR / f"{target_god_id}.png"

        if not template_path.exists():
            # Try without extension or with jpg
            for ext in ['.jpg', '.jpeg', '.webp']:
                alt_path = GODS_IMAGES_DIR / f"{target_god_id}{ext}"
                if alt_path.exists():
                    template_path = alt_path
                    break

        if not template_path.exists():
            # No template - use fallback
            return self._create_fallback_result(source_image, target_god_id, output_size)

        template = cv2.imread(str(template_path))
        if template is None:
            return self._create_fallback_result(source_image, target_god_id, output_size)

        if self.insightface_available:
            return self._swap_with_insightface(source_image, template, output_size)
        else:
            return self._overlay_face(source_image, template, output_size)

    def _swap_with_insightface(
        self,
        source: np.ndarray,
        template: np.ndarray,
        output_size: tuple
    ) -> Optional[np.ndarray]:
        """Perform actual face swap using InsightFace."""
        try:
            # Detect faces
            source_faces = self.app.get(source)
            template_faces = self.app.get(template)

            if len(source_faces) == 0:
                print("No face detected in source image")
                return None

            if len(template_faces) == 0:
                print("No face detected in template image")
                return self._overlay_face(source, template, output_size)

            # Swap faces
            source_face = source_faces[0]
            result = self.swapper.get(template, template_faces[0], source_face, paste_back=True)

            # Resize to output size
            result = cv2.resize(result, output_size)

            return result

        except Exception as e:
            print(f"Face swap error: {e}")
            return self._overlay_face(source, template, output_size)

    def _overlay_face(
        self,
        source: np.ndarray,
        template: np.ndarray,
        output_size: tuple
    ) -> np.ndarray:
        """
        Fallback: Create an artistic overlay effect.
        Blends the user's face with the template.
        """
        try:
            import mediapipe as mp

            # Resize images
            source_resized = cv2.resize(source, output_size)
            template_resized = cv2.resize(template, output_size)

            # Detect face in source
            mp_face_mesh = mp.solutions.face_mesh
            face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

            rgb_source = cv2.cvtColor(source_resized, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb_source)

            if results.multi_face_landmarks:
                # Create face mask
                h, w = source_resized.shape[:2]
                mask = np.zeros((h, w), dtype=np.float32)

                landmarks = results.multi_face_landmarks[0]
                face_oval = [10, 338, 297, 332, 284, 251, 389, 356, 454,
                           323, 361, 288, 397, 365, 379, 378, 400, 377,
                           152, 148, 176, 149, 150, 136, 172, 58, 132,
                           93, 234, 127, 162, 21, 54, 103, 67, 109]

                points = []
                for idx in face_oval:
                    lm = landmarks.landmark[idx]
                    points.append([int(lm.x * w), int(lm.y * h)])

                points = np.array(points, dtype=np.int32)
                cv2.fillConvexPoly(mask, points, 1.0)

                # Blur mask edges
                mask = cv2.GaussianBlur(mask, (51, 51), 0)
                mask = np.stack([mask] * 3, axis=-1)

                # Blend
                result = (source_resized * mask * 0.3 + template_resized * (1 - mask * 0.3)).astype(np.uint8)

                # Add artistic filter
                result = self._apply_artistic_filter(result)

                return result

        except Exception as e:
            print(f"Overlay error: {e}")

        # Ultimate fallback - just return styled template
        template_resized = cv2.resize(template, output_size)
        return self._apply_artistic_filter(template_resized)

    def _apply_artistic_filter(self, image: np.ndarray) -> np.ndarray:
        """Apply artistic filter to make the result look more mythical."""
        # Convert to float
        img_float = image.astype(np.float32) / 255.0

        # Increase contrast slightly
        img_float = np.clip((img_float - 0.5) * 1.2 + 0.5, 0, 1)

        # Add golden tint for mythical effect
        golden_overlay = np.array([0.05, 0.03, 0.0])  # BGR
        img_float = np.clip(img_float + golden_overlay, 0, 1)

        # Vignette effect
        h, w = image.shape[:2]
        x = np.linspace(-1, 1, w)
        y = np.linspace(-1, 1, h)
        X, Y = np.meshgrid(x, y)
        vignette = 1 - np.sqrt(X**2 + Y**2) * 0.3
        vignette = np.clip(vignette, 0.7, 1.0)
        vignette = np.stack([vignette] * 3, axis=-1)

        img_float = img_float * vignette

        return (img_float * 255).astype(np.uint8)

    def _create_fallback_result(
        self,
        source: np.ndarray,
        god_id: str,
        output_size: tuple
    ) -> np.ndarray:
        """Create a fallback result when no template is available."""
        # Create a styled version of the source image
        result = cv2.resize(source, output_size)
        result = self._apply_artistic_filter(result)

        # Add text overlay
        font = cv2.FONT_HERSHEY_SIMPLEX
        god_name = god_id.replace('_', ' ').title()

        # Add semi-transparent overlay at bottom
        overlay = result.copy()
        cv2.rectangle(overlay, (0, output_size[1] - 60), (output_size[0], output_size[1]),
                     (0, 0, 0), -1)
        result = cv2.addWeighted(result, 0.7, overlay, 0.3, 0)

        # Add god name
        text_size = cv2.getTextSize(god_name, font, 0.8, 2)[0]
        text_x = (output_size[0] - text_size[0]) // 2
        cv2.putText(result, god_name, (text_x, output_size[1] - 25),
                   font, 0.8, (255, 215, 0), 2)

        return result


def convert_to_bytes(image: np.ndarray, format: str = 'PNG') -> bytes:
    """Convert numpy image to bytes."""
    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    buffer = io.BytesIO()
    pil_image.save(buffer, format=format)
    return buffer.getvalue()


def convert_to_base64(image: np.ndarray, format: str = 'PNG') -> str:
    """Convert numpy image to base64 string."""
    import base64
    img_bytes = convert_to_bytes(image, format)
    return base64.b64encode(img_bytes).decode('utf-8')


# Singleton instance
_swapper: Optional[FaceSwapper] = None


def get_face_swapper() -> FaceSwapper:
    """Get or create the face swapper singleton."""
    global _swapper
    if _swapper is None:
        _swapper = FaceSwapper()
    return _swapper
