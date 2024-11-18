import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Settings")
                       
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Controls randomness in the output"
        )
        max_length = st.number_input(
            "Max Length",
            min_value=100,
            max_value=2000,
            value=1000,
            step=100,
            help="Maximum length of the generated response"
        )
        return temperature, max_length