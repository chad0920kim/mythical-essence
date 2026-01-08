"""
Face Swap Service
Uses fal.ai API for high-quality face swapping
"""
import os
import base64
import requests
import cv2
import numpy as np
from pathlib import Path
from typing import Optional
from PIL import Image
import io

from app.config import GODS_IMAGES_DIR, OUTPUT_IMAGE_SIZE


class FaceSwapper:
    """
    Face swapping service using fal.ai API.
    Provides high-quality face swap results.
    """

    def __init__(self):
        self.fal_api_key = os.getenv("FAL_API_KEY")
        self.fal_available = bool(self.fal_api_key)

        if not self.fal_available:
            print("FAL_API_KEY not set. Face swap will use fallback mode.")

    def _encode_image_to_base64(self, image: np.ndarray) -> str:
        """Encode numpy image to base64 data URL."""
        # Convert BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)

        buffer = io.BytesIO()
        pil_image.save(buffer, format='PNG')
        data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return f"data:image/png;base64,{data}"

    def _encode_file_to_base64(self, file_path: Path) -> str:
        """Encode image file to base64 data URL."""
        with open(file_path, "rb") as f:
            data = base64.b64encode(f.read()).decode("utf-8")

        ext = file_path.suffix.lower()
        mime_types = {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp"
        }
        mime = mime_types.get(ext, "image/png")

        return f"data:{mime};base64,{data}"

    def swap_face(
        self,
        source_image: np.ndarray,
        target_god_id: str,
        output_size: tuple = OUTPUT_IMAGE_SIZE
    ) -> Optional[np.ndarray]:
        """
        Swap face from source image onto god template using fal.ai.

        Args:
            source_image: User's image (BGR numpy array)
            target_god_id: ID of the god template to use
            output_size: Output image dimensions

        Returns:
            Result image with swapped face, or None if failed
        """
        # Find template image
        template_path = self._find_template(target_god_id)

        if template_path is None:
            print(f"No template found for {target_god_id}")
            return self._create_fallback_result(source_image, target_god_id, output_size)

        if self.fal_available:
            result = self._swap_with_fal(source_image, template_path)
            if result is not None:
                # Resize to output size
                result = cv2.resize(result, output_size)
                return result

        # Fallback to styled template
        return self._create_fallback_result(source_image, target_god_id, output_size)

    def _find_template(self, god_id: str) -> Optional[Path]:
        """Find template image for given god ID."""
        for ext in ['.png', '.jpg', '.jpeg', '.webp']:
            template_path = GODS_IMAGES_DIR / f"{god_id}{ext}"
            if template_path.exists():
                return template_path
        return None

    def _swap_with_fal(
        self,
        source_image: np.ndarray,
        template_path: Path
    ) -> Optional[np.ndarray]:
        """Perform face swap using fal.ai API."""
        try:
            # Encode images
            source_b64 = self._encode_image_to_base64(source_image)
            target_b64 = self._encode_file_to_base64(template_path)

            # Call fal.ai API
            response = requests.post(
                "https://fal.run/fal-ai/face-swap",
                headers={
                    "Authorization": f"Key {self.fal_api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "base_image_url": target_b64,  # Template (background)
                    "swap_image_url": source_b64   # Source (face to extract)
                },
                timeout=60
            )

            if response.status_code != 200:
                print(f"fal.ai API error: {response.status_code} - {response.text}")
                return None

            result = response.json()

            if "image" in result and "url" in result["image"]:
                image_url = result["image"]["url"]

                # Download result image
                img_response = requests.get(image_url, timeout=30)
                if img_response.status_code == 200:
                    # Convert to numpy array
                    nparr = np.frombuffer(img_response.content, np.uint8)
                    result_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                    return result_image

            print("No image in fal.ai response")
            return None

        except Exception as e:
            print(f"fal.ai face swap error: {e}")
            return None

    def _apply_artistic_filter(self, image: np.ndarray) -> np.ndarray:
        """Apply artistic filter to make the result look more mythical."""
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
        """Create a fallback result when face swap fails."""
        # Try to load and style the template
        template_path = self._find_template(god_id)

        if template_path is not None:
            template = cv2.imread(str(template_path))
            if template is not None:
                result = cv2.resize(template, output_size)
                return self._apply_artistic_filter(result)

        # Ultimate fallback - style the source image
        result = cv2.resize(source, output_size)
        result = self._apply_artistic_filter(result)

        # Add text overlay
        font = cv2.FONT_HERSHEY_SIMPLEX
        god_name = god_id.replace('_', ' ').title()

        overlay = result.copy()
        cv2.rectangle(overlay, (0, output_size[1] - 60), (output_size[0], output_size[1]),
                     (0, 0, 0), -1)
        result = cv2.addWeighted(result, 0.7, overlay, 0.3, 0)

        text_size = cv2.getTextSize(god_name, font, 0.8, 2)[0]
        text_x = (output_size[0] - text_size[0]) // 2
        cv2.putText(result, god_name, (text_x, output_size[1] - 25),
                   font, 0.8, (255, 215, 0), 2)

        return result


def convert_to_bytes(image: np.ndarray, format: str = 'PNG') -> bytes:
    """Convert numpy image to bytes."""
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)

    buffer = io.BytesIO()
    pil_image.save(buffer, format=format)
    return buffer.getvalue()


def convert_to_base64(image: np.ndarray, format: str = 'PNG') -> str:
    """Convert numpy image to base64 string."""
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
