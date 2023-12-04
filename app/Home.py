import streamlit as st

# Set page title and icon
st.set_page_config(page_title="InsideAirbnb Data Analysis", page_icon="🏡")

# Page content
st.title("Unlocking Insights from InsideAirbnb Data")
st.write("Welcome to our capstone academic project, where we delve deep into the treasure trove of data from InsideAirbnb, aligning with the mission of transparency and understanding within the vacation rental industry.")

# Add mission alignment section
st.header("Our Mission Alignment:")
st.write("InsideAirbnb is committed to providing data transparency and facilitating informed decisions in the Airbnb marketplace. Our project is rooted in this mission and aims to contribute to InsideAirbnb's goal by offering the following analyses:")

# Add links to analysis pages
st.subheader("Explore Our Analyses:")
ml_price_prediction_link = "[ML Price Prediction Analysis](link-to-streamlit-page)"
entire_vs_partial_index_link = "[Entire House vs. Partial House Index](link-to-streamlit-page)"
choropleth_map_link = "[Choropleth of Airbnb vs. Available Housing](link-to-streamlit-page)"
st.markdown(f"- {ml_price_prediction_link}")
st.markdown(f"- {entire_vs_partial_index_link}")
st.markdown(f"- {choropleth_map_link}")

# Add project image(s)
st.image("project_image.jpg", caption="InsideAirbnb Data Analysis")

# Footer
st.write("Join us on this journey to uncover valuable insights, contribute to data transparency, and foster an informed Airbnb community.")
