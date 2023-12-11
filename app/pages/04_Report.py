import streamlit as st
from page_func import *

# Set page title and icon
st.set_page_config(page_title="Impact of Airbnb on housing affordability", page_icon="🏡")

st.image("app/banner.png", width=700)

st.write("Hello, World!")


affordability_pressure_chart(2000, 344, 500)