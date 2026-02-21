import streamlit as st
from scrape import scrape_website

st.title("AURA - AI Web Scrapper")
url= st.text_input("Enter a Website URL:")

if st.button("Scrape Site"):
    # perform scraping action or indicate progress
    st.write("Scraping the website")
    result = scrape_website(url)
    print(result)