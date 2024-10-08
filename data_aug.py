# Image augmentation - to generate more data by modifying the original image
import imutils  # Importing imutils for image rotation and other image processing functions
import cv2  # Importing OpenCV for image processing
import numpy as np  # Importing numpy for numerical operations

# Read the original image from file
i = cv2.imread('dark.jpeg')

alpha = 1.04  # Scaling factor for contrast adjustment
c = 1  # Counter to keep track of image filenames

# Loop to generate multiple images by adjusting brightness (beta) while keeping contrast constant
for beta in range(25):  # Varying beta from 0 to 24 (to generate 25 images)
    new_image = cv2.convertScaleAbs(i, alpha=alpha, beta=beta)  # Adjust contrast and brightness
    cv2.imwrite('aug1/' + str(c) + '.jpg', new_image)  # Save the new image to the 'aug' directory
    c += 1  # Increment the counter for the next image filename

ii = 1  # Counter to keep track of rotated image filenames

# Loop to generate multiple images by rotating the original image at different angles
for r in np.linspace(-10, 10, 91):  # Varying rotation angle from -10 to +10 degrees (generating 91 images)
    rotated = imutils.rotate(i, r)  # Rotate the image by 'r' degrees
    cv2.imwrite('aug2/' + str(ii) + '.jpg', rotated)  # Save the rotated image to the 'aug' directory
    ii += 1  # Increment the counter for the next image filename
