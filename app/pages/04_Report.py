import streamlit as st
import pandas as pd
import numpy as np
from page_func import * 


import streamlit as st
import pandas as pd
import altair as alt



data = pd.read_csv('app/uszip_stats.csv')


# Streamlit UI
st.title('Rent Burden Distribution by Neighborhood')

# City selector
city = st.selectbox('Select a city', data['city'].unique())

# Filter data based on the selected city
city_data = data[data['city'] == city]

# Altair Chart
chart = alt.Chart(city_data).mark_bar().encode(
    x='neighbourhood_cleansed:N',
    y='rent_burden:Q',
    tooltip=['neighbourhood_cleansed', 'rent_burden']
).properties(
    width=700,
    height=400
)

st.altair_chart(chart, use_container_width=True)