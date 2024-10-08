# Image-Processing-Using-OpenCV

This repository contains various image processing scripts, covering operations such as image alignment, blurring, data augmentation, and illumination transforms using techniques like gamma correction and logarithmic transformation. These scripts provide practical solutions for enhancing and manipulating images for computer vision and machine learning tasks.

## Folder Contents

1. **ALIGN.py**
   - **Description**: This script aligns an image using four selected points from the image, transforming it into a rectangular form using perspective transformation.
   - **Key Techniques**: 
     - Perspective transformation using OpenCV's `cv2.getPerspectiveTransform`.
     - Image selection via `plt.ginput` for user-driven alignment.
     - Resulting transformation using `cv2.warpPerspective`.

2. **BLUR.py**
   - **Description**: Applies a simple blurring filter to an image, softening edges and reducing noise. The script showcases how to use OpenCV’s `cv2.blur` function to smooth images.
   - **Key Techniques**: 
     - Blurring images with customizable kernel size.
     - Displaying both original and blurred images using OpenCV's `cv2.imshow`.

3. **DATA_AUGMENTATION.py**
   - **Description**: A script that performs image augmentation to generate new data by adjusting brightness, contrast, and applying rotations. This is particularly useful for expanding datasets for machine learning models.
   - **Key Techniques**: 
     - Brightness and contrast adjustment using `cv2.convertScaleAbs`.
     - Image rotation using the `imutils.rotate` function.
     - Automated saving of the augmented images in specified directories.

4. **LOG_GAMMA_ILLUMINATION_TRANSFORMS.py**
   - **Description**: This script applies gamma correction and logarithmic transformation to enhance or modify image illumination. Additional utility functions are included for adding or multiplying factors to adjust brightness and contrast.
   - **Key Techniques**: 
     - Gamma correction using a lookup table for pixel intensity adjustment.
     - Logarithmic transformation to enhance image contrast.
     - Brightness and contrast manipulation using addition and multiplication factors.
