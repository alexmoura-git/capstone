import streamlit as st


# Set page title and icon
st.set_page_config(page_title="Impact of Airbnb on housing affordability", page_icon="🏡")

st.image("https://www.canva.com/design/DAF2XWtskBc/6U7Ugo-TpfjuQeUZnEjxxA/edit?utm_content=DAF2XWtskBc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton", width=800)



st.markdown("""**Context**

**The headwinds ahead for short term renters**  
It’s without question that we’re heading into uncertain waters economically and within the real estate sector overall. Interest rates are increasing, individual wallet shares for travel are going down (C and Oladipo, 2023) , and because of factors like interest rate resets, and even just a maturing marketplace, Airbnb rental prices are peaking (Sperance, 2022) (Mehta, 2023). In fact, in the overall peer-to-peer marketplace segment in the US may sneakily be hitting a level of maturity (Has the gig economy peaked?, 2023). In addition, economic pressures on travelers and the opening of foreign destinations post covid, threaten the level of booking volume many Airbnb owners anticipated seeing (Summer Travel Expectations Still Strong but Economic Pressure and Poor Travel Experience May Weaken Future Demand, 2023).

With that premise, it is more important than ever for Airbnb property owners to have strong guidance from a listing mechanism that helps them to find the ideal pricing across the competitive landscape within their area since factors such as mortgage payments, cleaning and upkeep, and others require owners to squeeze out the maximum level of profitability possible.

**Existing studies on predicting airbnb pricing based on available listing data**  
Analyzing Airbnb data and developing predicting pricing models is a topic of study with plenty of depth and commercially available products to assist with price discovery. By far the industry leader from a commercial standpoint is Airdna, which is powered by its own screen scraping tool and an XGBoost Classifier to identify similar properties on different listing sites to compile a beset in class data set on properties to form its prediction tools.

Less robust, but still exciting exercises using Inside Airbnb data have been captured on single cities such as Carrillo’s model using XGBoost Regression and adding in proximity to historical markers around Edinburgh (Carrillo, 2019), Lewis’s example using XGBoost for London based cities (Lewis, 2019), or even Lambda’s example utilizing a Random Forest Regression in Los Angeles. Throughout all the examples we’ve reviewed, the average r-squared score has sat between .65 to .73.

Where we are looking to take the next step in addition to these efforts is to build a model that utilizes a selection of different metros, as well as including LightGBM in addition to XGBoost and a bouquet of traditional regression methodologies. Our hope is that the increased speed as well as more complex tree structure will work well with our large datasets. Although overfitting does remain a concern. In addition, we are looking to limit our feature selection to just ….FILL IN HERE to create a model that unlike the alternatives mentioned above, can be used by non-machine learning experts who may only know a minor amount about their property and listing structure.

**The impacts of short term rentals on the housing market**  
Beyond just the impacts of achieving a positive ROI and finding an ideal location to invest in monetarily, the continuous trend of socially conscious investments otherwise known as ESG investing (considering environmental, social, and corporate governance factors into one’s investment strategy), continues to play a significant role in determ

""")