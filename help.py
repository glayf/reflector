
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from io import StringIO


def app():
    st.title("Help & Key")

    st.header("Metrics")
    st.text("Below is a comprehensive guide to help make the most of the 'Metrics & Insights' \ngathered through Reflector.")
   
    st.text("All graphs are interactive, can be downloaded individually. Double click to reset. \nHover over bar for specific value.")

    st.text("Individual highlighting per graph is useful in larger situations with 5+ \nparticipants.")


    st.header("Words Spoken + Time Spoken graphs")
    st.subheader("How is it calculated")

    st.text("The light grey line across the graph is calculated as the mean of total data \npresent.")

    st.header("WPM Graph")
    st.subheader("How is it calculated")
    st.text("The dotted line is the typical average WPM spoken for most clarity and retention.")


    st.header("Sentiment Graph")
    st.subheader("How is it calculated")
    st.text("This is calculated as average sentiment of speech across every word spoken \nby participant")
    st.text("0 is neutral - anything above is considered positive and anything below is negative")

    st.header("Insights")
    st.text("Insights are calculated against as a variance from the mean for each metric. Except \nfor WPM where insight is calculated as a variance from typical mean WPM.\nThis ensures dynamic insights which are tailored to your meeting.")



