# Streamlit frontend

import streamlit as st
import tempfile
from detector import view_parking


demo_path = "../data/Aerial View - Woburn Mall.mp4"
demo_mask_path = "../masks/Aerial View - Manual.png"


def main():
    #view_parking(footage_path)
    
    st.header("Fraqtory")
    st.subheader("Parking Spots")
    
    st.text("Upload both a video and its corresponding mask")
    video = st.file_uploader('Upload video', type = ["mp4"])
    mask = st.file_uploader('Upload video mask', type =["jpg", "png", "jpeg"],)

    if video is None or mask is None:
        video_path = demo_path
        mask_path = demo_mask_path
    else:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(video.read())
            video_path = tmp_file.name      

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(video.read())
            video_path = tmp_file.name 

    st_live = st.empty()
    info = st.empty()

    for frame, empty, total_spots in view_parking(video_path, mask_path):
        st_live.image(frame)
        info.write(f"Empty Spots: {empty} / Total Spots: {total_spots}")

        
if __name__ == "__main__":
    main()