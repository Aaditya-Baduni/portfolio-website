import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Aaditya Baduni")
    content = """
    Henlo! Or should I say woof? I make really basic apps for simpletons to use!\n
    So go ahead!
    """
    st.info(content)

st.write("Below you can find some of the apps that I have built using Python. Feel free to contact me (Actually, don't, it's just a formality to say this)!")