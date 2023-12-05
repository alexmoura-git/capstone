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

st.markdown("""# Challenges of Housing Affordability in America

In the United States, housing affordability has become a pressing issue affecting millions of people. This Markdown page discusses some of the key challenges associated with housing affordability, highlighting the importance of addressing these issues.

## The Rising Cost of Housing

One of the most significant challenges is the **escalating cost of housing**. Over the past few decades, the price of homes has outpaced income growth, making it increasingly difficult for individuals and families to afford suitable housing options.

<div class="callout warning">
  <p>**Callout**: Rising housing costs are creating a barrier to entry for many aspiring homeowners.</p>
</div>

## Income Inequality

**Income inequality** exacerbates housing affordability problems. Low-income households often struggle to find housing that is both safe and affordable, as their wages do not keep up with rising rent and home prices.

<div class="callout danger">
  <p>**Callout**: Income inequality results in housing instability for vulnerable populations.</p>
</div>

## Gentrification

**Gentrification** in urban areas can displace long-time residents and change the character of neighborhoods. As neighborhoods become more desirable, property values rise, pushing out lower-income residents who can no longer afford to live there.

<div class="callout info">
  <p>**Callout**: Gentrification can lead to cultural displacement and loss of community identity.</p>
</div>

## Lack of Affordable Rental Housing

The availability of **affordable rental housing** is limited in many regions. High demand and low supply contribute to skyrocketing rents, leaving renters financially strained.

<div class="callout success">
  <p>**Callout**: Creating policies to increase affordable rental housing is crucial to address this issue.</p>
</div>

## Government Policies

Government policies play a significant role in addressing housing affordability. Programs like **affordable housing subsidies** and **rent control** can help mitigate the challenges, but their effectiveness varies by location.

<div class="callout primary">
  <p>**Callout**: Advocacy for fair and effective housing policies is essential to create long-term solutions.</p>
</div>

## Conclusion

Housing affordability in America is a multifaceted issue that affects individuals and communities across the country. Addressing these challenges requires a combination of policy changes, community involvement, and a commitment to ensuring that everyone has access to safe and affordable housing.

<style>
/* Add custom CSS for callout styles */
.callout {
  margin: 20px 0;
  padding: 20px;
  border-radius: 4px;
}

.callout.warning {
  background-color: #ffe66d;
  border: 1px solid #ffdb4d;
}

.callout.danger {
  background-color: #ff6b6b;
  border: 1px solid #ff0000;
}

.callout.info {
  background-color: #6bb9ff;
  border: 1px solid #006eff;
}

.callout.success {
  background-color: #7bed9f;
  border: 1px solid #4CAF50;
}

.callout.primary {
  background-color: #e3e3e3;
  border: 1px solid #ccc;
}
</style>
""")