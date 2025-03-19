import cv2
import numpy as np

# Path to the video file
video_path = '../data/Aerial View - Woburn Mall.mp4'

# Initialize variables
rectangles = []
drawing = False
start_point = None

# Mouse callback function to draw rectangles
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_point, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            frame_copy = frame.copy()
            cv2.rectangle(frame_copy, start_point, (x, y), (0, 255, 0), 2)
            cv2.imshow("Frame", frame_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        rectangles.append((start_point, end_point))
        cv2.rectangle(frame, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Read the first frame
success, frame = cap.read()
if not success:
    print("Failed to read video")
    cap.release()
    exit()

# Create a window and set the mouse callback
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", draw_rectangle)

# Display the frame and wait for user to draw rectangles
print("Draw rectangles to create a mask. Press 'q' to finish.")
while True:
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('p'):
        success, frame = cap.read()


# Create a mask with the drawn rectangles
mask = np.zeros(frame.shape[:2], dtype=np.uint8)
for rect in rectangles:
    cv2.rectangle(mask, rect[0], rect[1], 255, -1)

# Save the mask to a file
cv2.imwrite('new.png', mask)

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Mask created and saved as 'mask.png'.")