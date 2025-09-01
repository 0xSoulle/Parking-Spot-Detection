from ultralytics import YOLO
import cv2

# load custom model with trained weights
model = YOLO("best.pt")
 
cap = cv2.VideoCapture(source="data/*")
# run inference for all files in the data dir
results = model(source="data/*",show=True, stream=True)


for result in results:
    result_log = open("result_log.txt", "rw")
    boxes = result.boxes  
    masks = result.masks  
    keypoints = result.keypoints  
    probs = result.probs 
    obb = result.obb

    result.show() 