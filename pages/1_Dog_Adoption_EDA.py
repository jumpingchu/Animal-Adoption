import streamlit as st
import pandas as pd
from model.pet_adoption_api import PetAdoptionAPI
from util.plotter import DogDataPlotter
from util.layout import col_left_right_component

TITLE = "台灣流浪狗數據分析"
FILE_PATH = "./data/dog_data_transformed.csv"

st.set_page_config(initial_sidebar_state="collapsed", page_title=TITLE, layout="wide")
st.title(TITLE)


@st.cache_data(max_entries=3)
def get_data(path):
    df = pd.read_csv(path, index_col=0)
    return df


df = get_data(FILE_PATH)
st.dataframe(
    df.head(),
    column_config={
        "album_file": st.column_config.ImageColumn("album_file"),
    },
)

dog_data_plotter = DogDataPlotter(df)

## 時間分析
tab_list = ["每年分佈", "每月分佈"]
tab_year, tab_month = st.tabs(tab_list)
with tab_year:
    fig = dog_data_plotter.yearly_bar(title=tab_list[0])
    md_text_list = [
        "##",
        "- 2023 年明顯遠高於其他年份，但無法確定是因為流浪動物今年大幅增加，還是政府今年開始積極登記流浪動物，需待更多資訊才能確認此原因。",
    ]
    col_left_right_component(fig, md_text_list)

with tab_month:
    fig = dog_data_plotter.monthly_bar(title=tab_list[1])
    md_text_list = [
        "- 整體來看，會發現 9~12 月拾獲較多流浪狗",
        "- 但若是拆成不同年份來看（下圖），就會注意到數據還是受 2023 年影響為主，所以增加的原因也是需要更多資訊才能確定。",
    ]
    col_left_right_component(fig, md_text_list)
    fig = dog_data_plotter.yearly_monthly_bar(title="2020 ~ 2023年每月分佈")
    st.plotly_chart(fig, use_container_width=True)

## 性別分析
tab_list = ["公母比例", "公母 VS. 體型"]
tab_gender, tab_gender_bodytype = st.tabs(tab_list)
with tab_gender:
    fig = dog_data_plotter.gender_pie(title=tab_list[0])
    md_text_list = ["- 整體公母差異並不大，分佈約是各半"]
    col_left_right_component(fig, md_text_list)

with tab_gender_bodytype:
    fig = dog_data_plotter.gender_bodytype_pie(title=tab_list[1])
    md_text_list = ["- 中大型犬皆為公狗多於母狗，僅有小型犬的母狗數量大於公狗"]
    col_left_right_component(fig, md_text_list)

## 品種分析
tab_list = [
    "品種比例",
    "品種比例（不含米克斯）",
]
tabs = st.tabs(tab_list)
with tabs[0]:
    fig = dog_data_plotter.breed_pie(title=tab_list[0])
    md_text_list = ["- 幾乎所有流浪狗的品種皆為米克斯"]
    col_left_right_component(fig, md_text_list)
with tabs[1]:
    fig = dog_data_plotter.breed_exclude_mix(title=tab_list[1])
    md_text_list = ["##", "##", "- 排除米克斯後，以貴賓犬、比特犬、柴犬、臘腸、瑪爾濟斯這些台灣常見寵物狗品種為主"]
    col_left_right_component(fig, md_text_list)

## 年齡分析
tab_list = [
    "年齡比例",
]
tabs = st.tabs(tab_list)
with tabs[0]:
    fig = dog_data_plotter.age_pie(title=tab_list[0])
    md_text_list = ["- 流浪狗多數皆已是成犬"]
    col_left_right_component(fig, md_text_list)
    fig = dog_data_plotter.age_bodytype_pie(title="體型 VS. 年齡")
    md_text_list = [
        "- 其中以大型犬的成犬/幼犬比例（98:2）最懸殊",
        "- 代表流浪的大型犬幾乎都已是成犬",
        "- 猜測大型犬因為體型大而不易飼養，導致被遺棄的可能性高",
    ]
    col_left_right_component(fig, md_text_list)

## 毛色分析
tab_list = [
    "毛色比例",
]
tabs = st.tabs(tab_list)
with tabs[0]:
    fig = dog_data_plotter.colour_pie(title=tab_list[0])
    md_text_list = ["- 多數為小黑與小黃", "- 前四名都是黑黃色為主的狗，佔了整體的四分之三"]
    col_left_right_component(fig, md_text_list)
