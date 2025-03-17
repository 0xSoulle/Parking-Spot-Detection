import cv2


def view_parking(footage_path) :

    cap = cv2.VideoCapture(footage_path)

    ret = True

    while ret:
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAlllWindows()