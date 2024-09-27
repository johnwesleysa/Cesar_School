import streamlit as st
from utils import BIG_MAC, CHICKEN

col1, col2 = st.columns(2)


with st.container():
    with col1:
        st.image(BIG_MAC, width=150)
        sl_burguers = st.toggle("Select Big Mac")
        

    with col2:
        st.image(CHICKEN, width=185)
        sl_burguers= st.toggle("Select Chicken")
        


