# Airbnb Impact on Rental Affordability - Responsitory Instructions
This is the repository of the Capstone project Airbnb Impact on Rental Affordability. The team is composed by Alex Moura and Ryan Thomas and has as primary objective to build a real time machine learning powered affordability prediction tool to help investors and renters/travelers to assess the potential impact that their decision to invest or stay in a short term rental may have in the overall housing affordability of the local community.


## Project Statement
With the proliferation of short-term rentals in major metropolitan areas offering new opportunities for income to property owners, we are looking to provide the first ever rental price prediction dashboard that also provides insights into neighborhood rental affordability to assist potential owners and renters to better understand the neighborhood composition in order to make conscientious investment decisions based not just on ROI, but also socio-economic impact. 

As we move into an era where investment criteria in publicly traded securities now is not solely based on income returns and asset appreciation, but also a new criterial known as Environmental, Social, and Corporate Governance (ESG), which takes into account the ability of an institution to act in a globally responsible manner, we believe that the same criteria can be applied to real estate investments in the short-term rental market. 

We also believe that it is important for potential short term renters to be able to assess and understand the potential impact of their travel lodging decision to the local community.

Our goal is to help guide both investors as well as renters in their quest for insight into their investment/rental ideal price range, as well as the impact to the surrounding community so they can make the best investment decision that aligns with their values. 


## How to use this repository and run its code
* Clone this repository into a local or remote environment
* run import_data.py - This imports the Insigde Airbnb data into your deployment enviroment
* run update_model.py - Updates and fine-tunes the prediction model and the scaler
* geocode.py - updates geocoding of uszip rental stats file
* deploy in your local, remote or streamlit cloud enviroment
    * Home page is Home.py and additional pages are in the /Pages Folder

App is published at [Airbnb Impact on Rental Affordability - Live App](https://mads-capstone-alex-ryan.streamlit.app/Pricing_and_Affordability_Predictor)

In addition to the production steps above we also performed EDA, Data cleasing, model selecting and feature selection as preparation for production in the notebook [Model Selection, Feature Selection and Tunning - Non Prod Steps.ipynb](https://github.com/alexmoura-git/capstone/blob/main/Model%20Selection%2C%20Feature%20Selection%20and%20Tunning%20-%20Non%20Prod%20Steps.ipynb) available in this repository.




## Data Access Statement
The datasets generated, manipulated, and analyzed during the current study are publicly available at the following locations:



| Data                         | Description|
|--------------------------------------|---------------|
| Inside Airbnb - listings and geojson files           | Inside Airbnb data is made available under license that the author does not have permission to share based on community guidelines not to republish the data. Access to the data is available at Inside Airbnb, http://insideairbnb.com/get-the-data and datasets utilized were from Q3, 2023.|
| HUD - Picture of Subsidized Households          | HUD’s data is available in the following repository as well as HUD’s website, https://www.huduser.gov/portal/datasets/pictures/files/Zipcode_2022_2020census.xlsx|
|Simplemaps - US Zip Code Database | Simplemaps data is made available under license and is not available for public redistribution. Please contact Ryan Thomas (ryanwt@umich.edu) or Alex Moura (moura@umich.edu) for review and access to the dataset. |

