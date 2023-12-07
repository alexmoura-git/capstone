import streamlit as st


# Set page title and icon
st.set_page_config(page_title="Impact of Airbnb on housing affordability", page_icon="🏡")

st.image("app/banner.png", width=700)



# Project Description
st.markdown("## Project Description:")
st.write("This website is part of the Capstone Project of the Masters of Applied Data Science Program of the University of Michigan. The team composed by Alex Moura and Ryan Thomas and has as the primary objective assess the impact of Aribnb rental to the affordability of the housing in several communities in the US market")

st.write("fwfwefwf kwoekfowekf \
         wwfwefwfwefwefwfwefwefw \
         wefwewfwfw")

### Mission Alignment
st.markdown("### Our Mission Alignment:")
st.write("InsideAirbnb is committed to providing data transparency and facilitating informed decisions in the Airbnb marketplace. Our project is rooted in this mission and aims to contribute to InsideAirbnb's goal by offering the following analyses:")

# Analysis 1: ML Price Prediction
st.markdown("1. **ML Price Prediction Analysis:**")
st.write("We've developed a machine learning model to predict Airbnb prices accurately. Our analysis helps hosts understand the factors influencing their pricing strategy, ensuring competitive rates and maximizing revenue.")
ml_price_prediction_link = "[Check out our interactive ML Price Prediction page here.](link-to-streamlit-page)"
st.markdown(ml_price_prediction_link)

# Analysis 2: Entire House vs. Partial House Index
st.markdown("2. **Entire House vs. Partial House Index:**")
st.write("To assist travelers in finding their ideal accommodations, we've created an index that compares entire houses to partial houses based on various parameters like price, amenities, and location.")
entire_vs_partial_index_link = "[Discover the insights on our Entire House vs. Partial House Index here.](link-to-streamlit-page)"
st.markdown(entire_vs_partial_index_link)

# Analysis 3: Choropleth of Airbnb vs. Available Housing
st.markdown("3. **Choropleth of Airbnb vs. Available Housing:**")
st.write("Explore a visual representation of Airbnb listings compared to available housing in different regions. Our choropleth maps provide an in-depth perspective on the distribution of Airbnb properties and their impact on the local housing market.")
choropleth_map_link = "[Explore the maps here.](link-to-streamlit-page)"
st.markdown(choropleth_map_link)

# Conclusion and Call to Action
st.write("Join us on this journey to uncover valuable insights, contribute to data transparency, and foster an informed Airbnb community.")

st.markdown("""# Welcome to the Capstone Project: "Impact of Airbnb Rentals on Housing Affordability"

## Introduction

Housing affordability in America has become an increasingly pressing issue, with numerous reports and studies highlighting the challenges faced by many residents in finding affordable housing. The dream of owning a home or renting at reasonable rates has become elusive for a significant portion of the population. In this capstone project, conducted as part of the MADS program at the University of Michigan, we, Alex Moura and Ryan Thomas, aim to shed light on the relationship between the rise of Airbnb and the ongoing crisis of housing affordability.

## The Housing Affordability Crisis

The United States has been grappling with a housing affordability crisis for years. According to a report by the National Low Income Housing Coalition (NLIHC), in 2020, there was not a single state where a full-time minimum-wage worker could afford a two-bedroom rental apartment at fair market rent. This alarming statistic underscores the severity of the problem, where low-income individuals and families are increasingly burdened by the cost of housing.

## The Airbnb Effect

Originally, Airbnb emerged as a platform for homeowners to share spare rooms or temporarily rent out their primary residences to travelers, offering an opportunity to earn extra income. However, as reported by [The New York Times](https://www.nytimes.com/), [The Guardian](https://www.theguardian.com/), and others, Airbnb has evolved significantly. Investors and commercial operators have seized the opportunity to buy up properties and convert them into short-term rentals, often removing them from the traditional housing market. This shift in usage has been identified as a significant factor contributing to the shortage of long-term rental housing, thereby exacerbating the housing affordability crisis.

## Our Data Source: InsideAirbnb

To investigate the impact of Airbnb on housing affordability, we rely on data from InsideAirbnb, an independent project that collects and analyzes Airbnb listing data in cities across the globe. InsideAirbnb provides us with a comprehensive dataset that allows us to examine the extent to which Airbnb listings have become commercialized and its implications for housing availability and affordability.

## Project Overview

Our capstone project is structured to explore and address the intricate relationship between Airbnb rentals and housing affordability:

1. **Housing Price Prediction Model**
   - On our first page, we present a machine learning model that predicts housing prices in selected cities. By comparing these predicted prices to various statistical indicators, we aim to infer the affordability of housing in those areas, while considering the evolving role of Airbnb.

2. **Affordability Index Visualization**
   - The second page showcases a visualization of our affordability index, drawing from a wealth of data sources, including government reports and housing market analyses. This index offers a visual representation of how Airbnb rentals might be affecting housing affordability in different regions.

3. **Technology Stack**
   - Our third page delves into the technology stack we employed for this project. We utilized Python libraries for data analysis, machine learning, and visualization, along with Streamlit for creating interactive presentations, and Git for version control and collaboration.

Our project is a testament to the commitment to addressing a critical issue that affects communities across the United States. By examining the evolving landscape of Airbnb rentals and their impact on housing affordability, we hope to contribute valuable insights to the ongoing discourse.

We encourage you to explore each page in detail, engage with our findings, and join us in the effort to better understand and mitigate the "Impact of Airbnb Rentals on Housing Affordability." Together, we can work towards more equitable and affordable housing solutions for all Americans.

""")