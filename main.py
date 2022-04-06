import introduction
import metrics
import help
import streamlit as st

hide = """
            <style>
            footer {
                visibility: hidden; 
                }
            footer:after {
                content:'Made by Layth Mehdi'; 
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
            }
            </style>
            """
st.markdown(hide, unsafe_allow_html=True)

PAGES = {
    "Introduction": introduction,
    "Metrics & Insights": metrics,
    "Help": help,

}

st.sidebar.title("Reflector")

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()