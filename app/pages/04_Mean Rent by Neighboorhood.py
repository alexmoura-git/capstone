import streamlit as st
import pandas as pd
import altair as alt

st.image("app/banner.png", width=700)
data = pd.read_csv('app/uszip_stats.csv')

st.markdown('#### Mean Rent By Neighborhood')

city = st.selectbox('Select a city', data['city'].unique())

city_data = data[data['city'] == city]

bars = alt.Chart(city_data).mark_bar().encode(
    y='neighbourhood_cleansed:N',
    x='rent_median:Q',
    tooltip=['neighbourhood_cleansed', 'rent_median']
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3
).encode(
    text=alt.Text('rent_median:Q', format='.2f')
)

chart = (bars + text).properties(
    width=800,
    height=800
)

st.altair_chart(chart, use_container_width=True)
