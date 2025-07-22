from cv2.gapi import video
from ultralytics import YOLO
from os import listdir


model = YOLO("best.pt")
# all data files
files = [f for f in listdir("data") if f.endswith(".mp4")]

video_index = 0
while(True):
    results = model(source="data/"+files[video_index],show=True)

    # loop through data dir
    video_index = video_index + 1
    if (video_index >= len(files)):
        video_index = 0
