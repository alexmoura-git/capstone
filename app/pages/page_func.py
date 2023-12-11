import altair as alt
import pandas as pd
import numpy as np
import streamlit as st



def affordability_pressure_chart(predicted_rent, median_rent, max_val):
    
    max_val=max(predicted_rent, median_rent, max_val)

    # Create Data Frame with Points
    data = pd.DataFrame({
        'Predicted AirbnB Income': [predicted_rent],
        'Neigboorhood Median Rent': [median_rent]
    })

    # Base chart 
    points = alt.Chart(data).mark_text(
        text='🏠', 
        fontSize=30,
        align='center'
    ).encode(
        x='Predicted AirbnB Income:Q',
        y='Neigboorhood Median Rent:Q'
    )


    # Create a DataFrame for the 45-degree line
    line_data = pd.DataFrame({'x': np.linspace(0, max_val, 100)})
    line_data['y'] = line_data['x']

    # Create the area chart
    area_chart = alt.Chart(line_data).mark_area(
        line={'color':'darkred'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='white', offset=0),
                   alt.GradientStop(color='red', offset=1)],
            x1=0,
            x2=1,
            y1=0,
            y2=1
        )
    ).encode(
    x=alt.X('x', axis=alt.Axis(title='Predicted AirbnB Income')),  # Removing x-axis title
    y=alt.Y('y', axis=alt.Axis(title='Neigboorhood Median Rent'))  # Setting y-axis title
)


    text = alt.Chart(pd.DataFrame({'x': [max_val * 0.95], 'y': [max_val * 0.05], 'text': ['Affordability Pressure Region']})).mark_text(
        align='right',
        baseline='bottom',
        fontSize=14,
        color='white'
    ).encode(
        x='x:Q',
        y='y:Q',
        text='text:N'
    )


    return_chart = (area_chart + points + text).configure_axis(
        grid=False
    )


    return return_chart 

chart = affordability_pressure_chart(2000, 344, 500)

st.altair_chart(chart, use_container_width=True)