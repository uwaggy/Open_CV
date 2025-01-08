import cv2  # Import OpenCV library

# Read the image 'lena.jpg'
image = cv2.imread('lena.jpg')

# Resize the image to quarter of its original width and height
# (image.shape[1] is width, image.shape[0] is height)
resized_image = cv2.resize(image, (image.shape[1] // 4, image.shape[0] // 4))

# Save the resized image to a new file
cv2.imwrite('lena_resized.jpg', resized_image)