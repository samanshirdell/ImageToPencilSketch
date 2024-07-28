# Pip3 (for python3) or pip (for python2 or lower) install opencv-python.
import cv2

image = cv2.imread("/home/saman/Pictures/Image.jpg")
# Grey Image
g_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted = 255 - g_image
# Blur Image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = 255 - blur
# Convert Sketch Image
sketch = cv2.divide(g_image, inverted_blur, scale=256.0)
# Image Write
cv2.imwrite("sketch_image.png", sketch)
# Image Show
cv2.imshow("Image", sketch)