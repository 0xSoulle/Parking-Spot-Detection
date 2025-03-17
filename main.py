# Streamlit frontend

import streamlit as sl
from model import view_parking
import os



def main():

    sl.header("Fraqtory")
    sl.subheader("Parking Spots")


    if sl.button("Next"):
        #view_parking("data\Aerial View - Woburn Mall.mp4")
        sl.video("data\Aerial View - Woburn Mall.mp4")
        



if __name__ == "__main__":
    main()