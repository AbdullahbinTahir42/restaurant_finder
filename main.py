import streamlit as st
from helper import restaurant_finder



st.title("Restaurant Finder")

cuisine = st.sidebar.selectbox("Select Cuisine", ["Italian", "Chinese", "Pakistani", "Mexican"])


if cuisine:
    response = restaurant_finder(cuisine)
    st.header(response['restaurant_name'])

    menu_items = response['menu_items'].split(",")
    st.subheader("Menu Items:")
    for item in menu_items:
        st.write(f"- {item}")
