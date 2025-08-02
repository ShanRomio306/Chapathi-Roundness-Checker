import cv2
import numpy as np

def calculate_roundness(image_path):
    # Load and resize image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (512, 512))

    # Convert to grayscale and blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding (Otsu)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply morphological closing to clean small gaps
    kernel = np.ones((5, 5), np.uint8)
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Find contours from the cleaned mask
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = [c for c in contours if cv2.contourArea(c) > 1000]  # Filter small noise

    if not contours:
        return 0

    # Use convex hull to smooth the edge
    largest = max(contours, key=cv2.contourArea)
    hull = cv2.convexHull(largest)

    area = cv2.contourArea(hull)
    perimeter = cv2.arcLength(hull, True)

    if perimeter == 0:
        return 0

    roundness = 4 * np.pi * area / (perimeter ** 2)
    return round(roundness * 100, 2)  # Percentage

def is_likely_chapati(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Detect brown color range
    lower_brown = np.array([10, 50, 50])
    upper_brown = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower_brown, upper_brown)

    brown_pixels = cv2.countNonZero(mask)
    total_pixels = img.shape[0] * img.shape[1]

    brown_ratio = brown_pixels / total_pixels

    # If brown pixels > 20%, assume it's a chapati
    return brown_ratio > 0.2
