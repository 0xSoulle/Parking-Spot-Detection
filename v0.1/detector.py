
import cv2
import numpy as np
from utils.filter import *

weights = "utils/yolov3.weights"
config = "utils/yolov3.cfg"

def get_parking_spots():  
    mask = cv2.imread("../masks/test.png", 0)

    p_spots_bounding_boxes = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    p_spots_positions = extract_spots_with_mask(p_spots_bounding_boxes)
    
    return len(p_spots_positions), p_spots_positions

def spot_availability(yolo, output_layers, cropping):
    blob = cv2.dnn.blobFromImage(cropping, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    yolo.setInput(blob)
    outs = yolo.forward(output_layers)

    car_detected = False
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if class_id == 2 and confidence > 0.5:  # Assuming '2' is the class ID for cars
                return True
        if car_detected:
            return True       

    return False

def view_parking(footage_path):

    cap = cv2.VideoCapture(footage_path)
    total_spots, spots_positions = get_parking_spots()
    
    ret = True
    pause = False

    yolo = cv2.dnn.readNet(weights, config)
    layer_names = yolo.getLayerNames()
    output_layers = [layer_names[i-1] for i in yolo.getUnconnectedOutLayers()]
    
    while ret:
        # to loop video 
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    	
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        if cv2.waitKey(25) & 0xFF == ord('p'):
            pause = not pause
        if not pause:
            ret, frame = cap.read()
        
        for spot in spots_positions:
            empty_counter = 0

            x1, y1, w, h = spot
            cropping = frame[y1:y1+h, x1:x1+w]

            if spot_availability(yolo, output_layers, cropping):
                cv2.rectangle(frame, (x1,y1), (x1 + w, y1 + h), (0,255,0),2)
                empty_counter += 1
            else:
                cv2.rectangle(frame, (x1,y1), (x1 + w, y1 + h), (0,0,255),2)

        #cv2.imshow('frame', frame)
        _,frame_buffer = cv2.imencode('.jpg', frame)
        frame_bytes = frame_buffer.tobytes()
        
        yield frame_bytes,empty_counter, total_spots
         
    cap.release()
    cv2.destroyAllWindows()