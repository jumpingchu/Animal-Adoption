import streamlit as st
import pandas as pd
from model.pet_adoption_api import PetAdoptionAPI
from plot.plotter import DogDataPlotter


st.set_page_config(initial_sidebar_state="collapsed")
st.title("台灣流浪狗數據分析")

df = pd.read_csv("./data/dog_data_transformed.csv", index_col=0)
df.insert(0, "album_file", df.pop("album_file"))

st.dataframe(
    df[:5],
    column_config={
        "album_file": st.column_config.ImageColumn("album_file"),
    },
)

## Graphs
dog_data_plotter = DogDataPlotter(df)
tab_year, tab_month = st.tabs(["每年分佈", "每月分佈"])
with tab_year:
    col_left, col_right = st.columns([3, 1])
    with col_left:
        fig = dog_data_plotter.yearly_plot()
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        ## 每年分佈
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("2023 年明顯遠高於其他年份，但無法確定是因為流浪動物今年大幅增加，還是政府今年開始積極登記流浪動物，需待更多資訊才能確認此原因。")

with tab_month:
    col_left, col_right = st.columns([3, 1])
    with col_left:
        fig = dog_data_plotter.monthly_plot()
        st.plotly_chart(fig, use_container_width=True)

    with col_right:
        ## 每年分佈
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.markdown("整體來看，會發現 9~12 月拾獲較多流浪狗")
        st.markdown("但若是拆成不同年份來看（下圖），就會注意到數據還是受 2023 年影響為主，所以增加的原因也是需要更多資訊才能確定。")
    
    fig = dog_data_plotter.multi_yearly_plot()
    st.plotly_chart(fig, use_container_width=True)
