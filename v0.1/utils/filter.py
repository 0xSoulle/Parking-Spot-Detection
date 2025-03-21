
# Filter to enhance lines and components of a frame

import cv2
import numpy

# enhance image caracteristics to better detect traffic lines
def enhance_frame(frame):
    # gray scale footage (enhances whites and blacks removing colour)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # apply gaussian blur to clear noise (white lines > flashes and shadows)
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)
    # 
    threshold = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    # 
    median = cv2.medianBlur(threshold, 5)
    kernel = numpy.ones((3, 3), numpy.uint8)

    return cv2.dilate(median, kernel, iterations=1)

# using a mask overlay get position in-frame from parking spots
def extract_spots_with_mask(bounding_boxes):
    
    (total_boxes, labels_id, values, centroid) = bounding_boxes

    parking_spots = []
    coef = 1  

    # from each parking spot outline box get the dimensions and position of the slot
    for spot_box in range(1, total_boxes):
        x1 = int(values[spot_box, cv2.CC_STAT_LEFT] * coef)
        y1 = int(values[spot_box, cv2.CC_STAT_TOP] * coef)
        w = int(values[spot_box, cv2.CC_STAT_WIDTH] * coef)
        h = int(values[spot_box, cv2.CC_STAT_HEIGHT] * coef)
        
        parking_spots.append([x1,y1,w,h])

    return parking_spots

