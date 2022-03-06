import streamlit as st

if st.button("Submit")
    st.write("Submitted!")
    
st.text_input("Name")

st.radio("Radio Buttons", ['a', 'b', 'c'], index = 0)

st.selectbox("Select Box", ['a', 'b', 'c'], index = 0)

st.slider("Age", min_value = 10,
          max_value = 30,
          value = 15,
          step = 2)

st.file_uploader("Upload a File Here")


