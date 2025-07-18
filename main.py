import cv2 
from os import listdir

files = [f for f in listdir("data") if f.endswith(".mp4")]


# Infinite loop through video files
video_index = 0
while True:
    video_path = "data/" + files[video_index]
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Failed to open video: {video_path}")
        break

    print(f"Now playing: {video_path}")


    if (cv2.waitKey(34) == ord("q")):
        break

    pause = False
    while (cap.isOpened()):
        key = cv2.waitKey(34)
        # capture keyboard presses (explicitly sets framerate with wait delay in this case 33ms -> 30fps)
        # Pressing "q" will stop the video
        if key == ord("q"):
            exit("EXITING BY USER REQUEST")
        # Pressing "n" will skip the current video
        elif key == ord("n"):
            break   
        # Pressing "p" will pause the video
        elif key == ord('p'): 
            pause = not pause
        if not pause :
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Frame", frame)
    video_index = video_index + 1
    if (video_index >= len(files)):
        video_index = 0

cap.release()
cv2.destroyAllWindows()