# Load libraries needed
import streamlit as st
 
# Set page configuration
st.set_page_config(
    page_title="Welcome To The Time Series App",
    page_icon="😃",
    layout="wide"
)
 
# Create a sidebar to select pages
page = st.sidebar.radio("Select a page:", ("Home", "Forecast Sales", "View Dataset", "About Team"))
 
# Add content to your Streamlit app based on the selected page
if page == "Home":
    st.markdown("# 👋 Welcome To Team Cape Cod's Sales Forecasting App Of Products Across Favorita stores")
    st.image("https://www.animatedimages.org/data/media/1645/animated-waving-image-0090.gif")
    st.write("""
<style>
            @keyframes slide-in {
                0% {
                    transform: translateX(-100%);
                }
                100% {
                    transform: translateX(0);
                }
            }
            .slide-in-animation {
                animation: slide-in 1.5s ease-in-out;
            }
</style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="slide-in-animation">Favorita Corporation is an Ecuador-based company engaged in the organization, installation, and administration of stores, markets, and supermarkets. The company has a business presence in many international countries also. This app, with the help of a linear regression model, will enable you to predict sales across Favorita Stores.</div>', unsafe_allow_html=True)
 
if page == "Forecast":
    # Add content for the "Forecast Sales" page
    st.markdown("## Forecast Sales Page Content")
    # Add your content for this page here
 
if page == "Explore":
    # Add content for the "View Dataset" page
    st.markdown("## View Dataset Page Content")
    # Add your content for this page here
 
if page == "About":
    # Add content for the "About Team" page
    st.markdown("## About Team Page Content")
    # Add your content for this page here