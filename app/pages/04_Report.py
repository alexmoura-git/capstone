import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
import altair as alt



data = pd.read_csv('app/uszip_stats.csv')


st.title('Rent Burden Distribution by Neighborhood')

# City selector
city = st.selectbox('Select a city', data['city'].unique())


city_data = data[data['city'] == city]


bars = alt.Chart(city_data).mark_bar().encode(
    x='neighbourhood_cleansed:N',
    y='rent_burden:Q',
    tooltip=['neighbourhood_cleansed', 'rent_burden']
)

text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=-5  
).encode(
    text=alt.Text('rent_burden:Q', format='.1f%') 
)

# Combine 
chart = (bars + text).properties(
    width=700,
    height=400
)

st.altair_chart(chart, use_container_width=True)