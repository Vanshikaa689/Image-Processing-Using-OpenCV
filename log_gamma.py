import numpy as np  # Importing numpy for numerical operations
import cv2  # Importing OpenCV for image processing

# Function to apply gamma correction to an image
def gamma_corr(image, gamma):
    invGamma = 1.0 / gamma  # Calculate the inverse of the gamma value
    # Create a lookup table to map pixel values based on gamma correction
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    # Apply gamma correction using the lookup table
    return cv2.LUT(image, table)

# Function to apply logarithmic transformation to an image
def log_transform(image, c):
    # Create a lookup table to map pixel values based on log transformation
    # The formula used is c * log(1 + image)
    table = np.array([(np.log((i / 255.0) + 1) * c) * 255 for i in np.arange(0, 256)]).astype("uint8")
    # Apply log transformation using the lookup table
    return cv2.LUT(image, table)

# Function to add a constant factor to an image
def img_add(image, factor):
    # Add the factor to the image and apply normalization (0-255) after addition
    return np.clip(image + factor, 0, 255).astype("uint8")

# Function to multiply a constant factor with an image (change contrast)
def img_mul(image, factor):
    # Multiply the image by the factor and apply normalization (0-255) after multiplication
    return np.clip(image * factor, 0, 255).astype("uint8")

# Read the image from file
i = cv2.imread('dark.jpeg')

# Apply gamma correction with gamma = 0.5
i_corr1 = gamma_corr(i, 0.5)

# Apply logarithmic transformation with c = 1.5
i_corr2 = log_transform(i, 1.5)

cv2.imshow('orig',i)
cv2.waitKey(0)

cv2.imshow('gamma=0.5',i_corr1)
cv2.waitKey(0)

cv2.imshow('log',i_corr2)
cv2.waitKey(0)
