import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    print("Image Shape:", image.shape)