from ultralytics import YOLO
import cv2

model = YOLO("best.pt")
cap = cv2.VideoCapture("data")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    for result in results:
        box = result.box
        names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # class name of each box
        confs = result.boxes.conf  # confidence score of each box
        for box in box:
            #print(box)
            x, y, w, h = box.xywhn[0].tolist()

            # draw green rectangle for empty
            if names[box] == "empty":
                cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 2)

            # draw red rectangle for occupied
            # cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)

    #cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

