# Assignment Date: 08/04/2026
# Assignment Name: Image Filter Lab
# Description: Use OpenCV to grayscale, blur, detect edges and show
# before/after.

import os
import numpy as np
import cv2


def build_sample_image(out_path: str) -> None:
    """Draw a simple image with shapes so filters have something to work on."""
    img = np.full((240, 320, 3), 240, dtype=np.uint8)  # light grey bg
    cv2.rectangle(img, (40, 40), (140, 140), (0, 0, 255), -1)          # red box
    cv2.circle(img, (220, 100), 50, (0, 180, 0), -1)                    # green circle
    cv2.line(img, (20, 200), (300, 200), (255, 0, 0), 4)               # blue line
    cv2.putText(img, "OpenCV", (40, 220),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imwrite(out_path, img)


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    original_path = os.path.join(here, "27_original.png")
    gray_path = os.path.join(here, "27_grayscale.png")
    blur_path = os.path.join(here, "27_blur.png")
    edges_path = os.path.join(here, "27_edges.png")
    combo_path = os.path.join(here, "27_before_after.png")

    if not os.path.exists(original_path):
        build_sample_image(original_path)

    img = cv2.imread(original_path)
    if img is None:
        raise FileNotFoundError("Could not load image")

    # 1. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 2. Blur
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    # 3. Edges
    edges = cv2.Canny(blur, 50, 150)

    cv2.imwrite(gray_path, gray)
    cv2.imwrite(blur_path, blur)
    cv2.imwrite(edges_path, edges)

    # Build a before/after side-by-side (convert single-channel back to BGR)
    def to_bgr(g):
        return cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)

    strip = cv2.hconcat([img, to_bgr(gray), to_bgr(blur), to_bgr(edges)])
    cv2.imwrite(combo_path, strip)

    print("Saved:")
    for p in [original_path, gray_path, blur_path, edges_path, combo_path]:
        print(" -", p)

    print("\n--- What each filter does ---")
    print(
        "Grayscale: collapses BGR into a single intensity channel (0-255).\n"
        "Blur     : smooths noise using a Gaussian kernel; useful as a\n"
        "           pre-processing step before edge detection.\n"
        "Canny    : finds regions where the intensity changes sharply -\n"
        "           the edges of objects in the image."
    )


if __name__ == "__main__":
    main()
