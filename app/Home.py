import streamlit as st


# Set page title and icon
st.set_page_config(page_title="Impact of Airbnb on housing affordability", page_icon="🏡")

st.image("app/banner.png", width=700)



st.markdown("""## Project Description

This website is part of the Capstone Project of the **Masters of Applied Data Science** Program of the **University of Michigan**. The team is composed by **Alex Moura** and **Ryan Thoma**s and has as primary objective to build a real time machine learning powered affordability prediction tool to help investors and renters/travelers to assess the potential impact that their decision to invest or stay in a short term rental may have in the overall housing affordability of the local community.

## Context and Motivation

Although the original concept of Airbnb started as a clever way to rent available idle space in people’s homes to travelers and event goes generating additional income to hosts and affordable lodging to travelers, the company created a new industry that has become a popular real estate investment opportunity. This is sparked a broad discussion about the topic and in 2019 the Economic Policy Institute conducted a study that concluded “that the costs of Airbnb outweighs the benefits” citing the impacting on housing affordability as one of the main negative externalities driving this costs which also included loss of taxation revenue and impact on the local lodging labor market. The economic costs and benefits of Airbnb: No reason for local policymakers to let Airbnb bypass tax or regulatory obligations. (n.d.). Economic Policy Institute. See report [HERE](https://www.epi.org/publication/the-economic-costs-and-benefits-of-airbnb-no-reason-for-local-policymakers-to-let-airbnb-bypass-tax-or-regulatory-obligations).

With the proliferation of short-term rentals in major metropolitan areas offering new opportunities for income to property owners, we are looking to provide a rental price prediction dashboard that also provides insights into neighborhood rental affordability to assist potential owners and renters to better understand the neighborhood composition in order to make conscientious investment decisions. We aim to help investors be aware of the potential impact that their decision to purchase a property may have in the overall affordability of homes in the local communities. We also aim to inform potential short term renters of the same impact.  We hope that our tool can help investor and renters better align their investment and travel lodging decisions to their values.


## Our data
To investigate the impact of Airbnb on housing affordability, we rely on data from InsideAirbnb, an independent project that collects and analyzes Airbnb listing data in cities across the globe. InsideAirbnb provides us with a comprehensive dataset that allows us to examine the extent to which Airbnb listings have become commercialized and its implications for housing availability and affordability.

## Project Navigation
Our capstone project is structured to explore and address the intricate relationship between Airbnb rentals and housing affordability:
1.	[Pricing and Affordability Predictor](/Pricing_and_Affordability_Predictor)
o	On our first page, we present a machine learning model that predicts housing prices in selected cities. 
2.	Affordability Index Visualization
o	The second page showcases a visualization of our affordability index.This index offers a visual representation of how Airbnb rentals might be affecting housing affordability in different regions.
3.	Technology Stack
o	Our third page delves into the technology stack we employed for this project. We utilized Python libraries for data analysis, machine learning, and visualization, along with Streamlit for creating interactive presentations, and Git for version control and collaboration.

Join us on this journey to uncover valuable insights, contribute to data transparency, and foster an informed Airbnb community.

""")