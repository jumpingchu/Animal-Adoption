import plotly.express as px
import streamlit as st

def col_left_right_component(fig, md_text_list: list[str], cols_spec: list = [2, 1]):
    col_left, col_right = st.columns(cols_spec)
    with col_left:
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        for text in md_text_list:
            st.markdown(text)
