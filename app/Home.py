import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Unlocking Insights from InsideAirbnb Data", page_icon="🏡")

# Project Description
st.markdown("## Project Description:")
st.write("Welcome to our capstone academic project, where we delve deep into the treasure trove of data from InsideAirbnb, aligning with the mission of transparency and understanding within the vacation rental industry. Through meticulous analysis and cutting-edge machine learning techniques, we've embarked on a journey to empower both hosts and travelers with valuable insights.")

# Mission Alignment
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
