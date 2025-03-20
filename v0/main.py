# Streamlit frontend

import streamlit as sl
from model import view_parking



def main():
    view_parking("../data/Aerial View - Woburn Mall.mp4")
    
    sl.header("Fraqtory")
    #l.subheader("Parking Spots")


    if sl.button("Next"):
        sl.video(view_parking("data/Aerial View - Woburn Mall.mp4"))
        



if __name__ == "__main__":
    main()