# Assignment Date: 06/04/2026
# Assignment Name: Image as Numbers
# Description: Load an image, print shape, pixel values, channels, and explain
# them.

import os
import numpy as np
import cv2


def build_sample_image(out_path: str) -> None:
    """Create a small RGB test image (100x120) with coloured bands."""
    img = np.zeros((100, 120, 3), dtype=np.uint8)
    img[:, :40] = [255, 0, 0]        # Blue band   (OpenCV uses BGR!)
    img[:, 40:80] = [0, 255, 0]      # Green band
    img[:, 80:] = [0, 0, 255]        # Red band
    cv2.imwrite(out_path, img)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(here, "26_sample_image.png")
    if not os.path.exists(img_path):
        build_sample_image(img_path)
        print(f"Created sample image at {img_path}")

    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Could not load image: {img_path}")

    print("--- Image Info ---")
    print(f"File     : {img_path}")
    print(f"Shape    : {img.shape}   (height, width, channels)")
    print(f"Dtype    : {img.dtype}")
    print(f"Min / Max pixel value: {img.min()} / {img.max()}")

    h, w, c = img.shape
    print(f"Height   : {h}px")
    print(f"Width    : {w}px")
    print(f"Channels : {c}  (OpenCV loads in BGR order)")

    # A few sample pixels
    print("\n--- Sample pixel values ---")
    for (y, x) in [(0, 0), (0, 60), (0, 100), (50, 50)]:
        b, g, r = img[y, x]
        print(f"Pixel ({y},{x}) -> B={b}, G={g}, R={r}")

    print("\n--- Explanation ---")
    print(
        "A digital image is just a 3D array of numbers.\n"
        " * Height and width give the 2D grid size.\n"
        " * Each cell is a pixel holding 3 numbers (Blue, Green, Red in\n"
        "   OpenCV) ranging 0-255.\n"
        " * The value represents intensity of that colour. (0,0,255) means\n"
        "   pure red.\n"
        " * Grayscale images drop the channel dimension and become a 2D\n"
        "   matrix with one intensity per pixel."
    )


if __name__ == "__main__":
    main()
