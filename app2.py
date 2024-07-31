import cv2
import numpy as np

def detect_fake_currency(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to create a binary image
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # If the area is below a certain threshold, consider it a counterfeit
        if area < 1000:
            cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

    # Display the result
    cv2.imshow("Counterfeit Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "D:\\Downloads\\100.jpg"  # Replace with the path to your banknote image
    detect_fake_currency(image_path)
