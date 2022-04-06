import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from io import StringIO


def app():
    st.header("Welcome to Reflector!")
    st.text("Reflector is a dashboard designed to give you meaningful insight into your \nMicrosoft Teams meetings.")
    st.text("To get started analysing your meeting, you'll first need to download the WebTTV \ntranscript file (.vtt) from your meeting.")

    st.text("For instructions on how to find and download this file, click the box below!")

    my_expander = st.expander("How to find your transcript:", expanded=True)

    with my_expander:
        st.text("In Microsoft Teams, once a meeting has concluded, a transcript file will \nbe generated, whether in the desktop app or the web version. These will appear \nin the chat log and can be downloaded to your computer.")
        st.text("1. Open your Teams dashboard and select the chat section.")
        st.text("2. Search for the meeting you would like to analyse and locate the trasncript.")
        st.text("3. Click the 'three dots' icon in the top-right file of the transcript and \nselect 'Download as .vtt'")
        st.text("4. The file will appear in your downloads folder and can now be uploaded.")

    st.text("To upload your file for analysis, navigate to the 'Metrics' on the left.")
