import streamlit as st


st.write("Hello, World more!")

df = pd.read_pickle('app/all_cities_filtered.pkl')
df


def page_home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

# Page 2
def page_about():
    st.title("About Page")
    st.write("This is the About Page!")

# Page 3
def page_contact():
    st.title("Contact Page")
    st.write("You can reach us at contact@example.com.")
    
    
    
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "About", "Contact"])

    if page == "Home":
        page_home()
    elif page == "About":
        page_about()
    elif page == "Contact":
        page_contact()

if __name__ == "__main__":
    main()