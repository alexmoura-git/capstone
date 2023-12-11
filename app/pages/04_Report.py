import streamlit as st
import pandas as pd
import numpy as np
from page_func import * 


# Set page title and icon
st.set_page_config(page_title="Impact of Airbnb on housing affordability", page_icon="🏡")

st.image("app/banner.png", width=700)

st.write("Hello, World!")

chart = affordability_pressure_chart(2000, 344, 500)

st.altair_chart(chart, use_container_width=True)


