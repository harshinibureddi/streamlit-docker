import streamlit as st

st.markdown(
    "<h3 style='margin-bottom:-3%;color: Black'>Hi there!</h3>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='color: Black'>Welcome to *Virtual Diagnosis*</h4>",
    unsafe_allow_html=True
)
st.markdown(
    "<h6 style='color:black,margin-left:10%'>&nbsp;&nbsp;&nbsp;&nbsp;This app is meant to assist medical professionals ONLY</h6>",
    unsafe_allow_html=True
)
st.text_input('Name of the patient? (*Try to keep the symptoms meaningful*)')
st.button("Submit")