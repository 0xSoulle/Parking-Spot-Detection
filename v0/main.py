# Streamlit frontend

import streamlit as st
from detector import view_parking

footage_path = "../data/Aerial View - Woburn Mall.mp4"

def main():
    #view_parking(footage_path)
    
    st.header("Fraqtory")
    st.subheader("Parking Spots")

    st_frame = st.empty()

    for frame in view_parking(footage_path):
        st_frame.image(frame)
        



if __name__ == "__main__":
    main()