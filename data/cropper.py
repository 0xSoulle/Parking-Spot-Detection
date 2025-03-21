import cv2
import numpy as np

def extract_crops_from_image(image_path, mask_path):
    # Load the image and mask
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    
    # Ensure the mask is binary
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    
    # Find connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    
    # Extract each region using the bounding boxes
    for i in range(1, num_labels):  # Start from 1 to skip the background
        x, y, w, h, area = stats[i]
        crop = image[y:y+h, x:x+w]
        
        # Display or process the crop
        cv2.imwrite(f'crops/crop {i}.png', crop)
    
    cv2.destroyAllWindows()

# Usage
image_path = "frame.png"
mask_path = "../masks/Aerial View - Manual.png"
extract_crops_from_image(image_path, mask_path)