import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import altair as alt


st.image("app/banner.png", width=700)
data = pd.read_csv('app/uszip_stats.csv')



st.markdown ('#### Rent Burden Distribution by Neighborhood')

# City selector
city = st.selectbox('Select a city', data['city'].unique())

# Filter data 
city_data = data[data['city'] == city]


bars = alt.Chart(city_data).mark_bar().encode(
    y='neighbourhood_cleansed:N',
    x='rent_burden:Q',
    tooltip=['neighbourhood_cleansed', 'rent_burden']
)


text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  #
).encode(
    text=alt.Text('rent_burden:Q', format='.1f')  
)

# Combine the bars and text
chart = (bars + text).properties(
    width=800,  #
    height=800
)

st.altair_chart(chart, use_container_width=True)