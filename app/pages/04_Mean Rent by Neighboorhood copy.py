import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import altair as alt



data = pd.read_csv('app/uszip_stats.csv')



st.markdown('#### Mean Rent By Neighboorhood')

# City selector
city = st.selectbox('Select a city', data['city'].unique())

# Filter data 
city_data = data[data['city'] == city]


bars = alt.Chart(city_data).mark_bar().encode(
    y='neighbourhood_cleansed:N',
    x='rent_mean:Q',
    tooltip=['neighbourhood_cleansed', 'rent_mean']
)


text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  #
).encode(
    text=alt.Text('rent_mean:Q', format='.2f')  
)

# Combine the bars and text
chart = (bars + text).properties(
    width=800,  #
    height=800
)

st.altair_chart(chart, use_container_width=True)