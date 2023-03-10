import streamlit as st

st.set_page_config(page_title="Hello World", page_icon="👌")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("ETL Generator")
st.header("Welcome")

activities = ["Login", "About"]
choices = st.sidebar.selectbox("Select Activity", activities)
