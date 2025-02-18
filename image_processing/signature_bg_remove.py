import cv2
import numpy as np
import os
from PIL import Image


def remove_white_background(image_path, save_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Check if the image was loaded correctly
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return  # Skip this file

    # Convert grayscale images to BGR
    if len(img.shape) == 2:  # Grayscale image
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Convert to grayscale for background detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply threshold to detect white background
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Create an alpha channel with an inverted mask (255-white, 0-transparent)
    alpha = cv2.bitwise_not(mask)

    # Ensure the image has exactly 3 color channels (BGR)
    if img.shape[2] == 4:  # Image already has an alpha channel
        b, g, r, _ = cv2.split(img)
    else:  # Image is BGR, add an alpha channel
        b, g, r = cv2.split(img)

    # Merge BGR channels with the new alpha channel
    final_img = cv2.merge([b, g, r, alpha])

    # Save the transparent image in PNG format
    cv2.imwrite(save_path, final_img)

def process_all_signatures(input_folder, raw_signatures):
    output_folder = os.path.abspath("./processed_data/signatures")
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist
    processed_data = []

    for raw_signature in raw_signatures:
        if raw_signature.endswith(".png"):  # Process only PNG files
            input_path = os.path.join(input_folder, raw_signature)
            output_path = os.path.join(output_folder, raw_signature)
            fix_png_image(input_path)

            remove_white_background(input_path, output_path)
            processed_data.append(output_path)

    return processed_data

def fix_png_image(image_path):
    img = Image.open(image_path)
    img.save(image_path, format="PNG", icc_profile=None)