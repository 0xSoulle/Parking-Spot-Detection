
import cv2
import torch
from tools.filter import *

weights = 'tools/weights.pt'

def get_parking_spots():  
    mask = cv2.imread("../masks/Aerial View - Manual.png", 0)

    p_spots_bounding_boxes = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
    p_spots_positions = extract_spots_with_mask(p_spots_bounding_boxes)
    
    return len(p_spots_positions), p_spots_positions

def spot_availability(yolo, cropping):
    results = yolo(cropping)

    detections = results.pandas().xyxy[0]
    
    if not detections.empty:
        return True
    
    return False

def view_parking(footage_path):

    cap = cv2.VideoCapture(footage_path)
    total_spots, spots_positions = get_parking_spots()
    
    ret = True
    pause = False

    #yolo = torch.hub.load('yolov5', 'custom', path=weights, source='local',force_reload=True)
    yolo = torch.hub.load('yolov5', 'custom',path = weights, source='local', force_reload=True)

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

            if spot_availability(yolo, cropping):
                cv2.rectangle(frame, (x1,y1), (x1 + w, y1 + h), (0,255,0),2)
                empty_counter += 1
            else:
                cv2.rectangle(frame, (x1,y1), (x1 + w, y1 + h), (0,0,255),2)

        #cv2.imshow('frame', frame)
        _,frame_buffer = cv2.imencode('.png', frame)
        frame_bytes = frame_buffer.tobytes()
        
        yield frame_bytes,empty_counter, total_spots
         
    cap.release()
    cv2.destroyAllWindows()