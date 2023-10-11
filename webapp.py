import streamlit as st
import camera_feed

def main():
    st.set_page_config(page_title="Streamlit WebCam App")
    st.title("Webcam Display Steamlit App")
    st.caption("Powered by OpenCV, Streamlit")
   
    frame_placeholder = st.empty()
    stop_button_pressed = st.button("Stop")
    camera_feed.take_feed(frame_placeholder, stop_button_pressed)

if __name__ == "__main__":
    main()