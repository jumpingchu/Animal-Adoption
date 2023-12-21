import plotly.express as px
import pandas as pd


class DogDataPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def groupby_count_preprocess(
        self,
        groupby_cols: list | str,
        query: str = None,
        rename_cols_dict: dict = {"animal_id": "Count"},
    ):
        if query:
            count_df = self.df.query(query)
        else:
            count_df = self.df.copy()
        count_df = count_df.groupby(groupby_cols, as_index=False).count()
        count_df = count_df.rename(columns=rename_cols_dict)
        return count_df

    def yearly_bar(self, title: str):
        target_col = "year"
        count_df = self.groupby_count_preprocess("year")
        fig = px.bar(
            count_df,
            x=target_col,
            y="Count",
            title=title,
            text_auto=True,
        )
        fig.update_xaxes(dtick=1)
        return fig

    def monthly_bar(self, title: str):
        target_col = "month"
        count_df = self.groupby_count_preprocess("month")
        fig = px.bar(count_df, x=target_col, y="Count", title=title, text_auto=True)
        fig.update_xaxes(dtick=1)
        return fig

    def yearly_monthly_bar(self, title: str):
        target_col = "month"
        facet_row = "year"
        year_range = list(range(2020, 2024))
        count_df = self.groupby_count_preprocess(
            [target_col, facet_row], query=f"year in {year_range}"
        )
        fig = px.bar(
            count_df,
            x=target_col,
            y="Count",
            title=title,
            color="Count",
            facet_row=facet_row,
            facet_row_spacing=0,
            text_auto=True,
        )
        fig.update_layout(height=600)
        fig.update_xaxes(dtick=1)
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
        return fig

    def gender_pie(self, title: str):
        target_col = "animal_sex"
        count_df = self.groupby_count_preprocess(target_col)
        fig = px.pie(
            count_df,
            names=target_col,
            values="Count",
            title=title,
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        return fig

    def gender_bodytype_pie(self, title: str):
        target_col = "animal_sex"
        facet_col = "animal_bodytype"
        count_df = self.groupby_count_preprocess([target_col, facet_col])
        fig = px.pie(
            count_df, names=target_col, values="Count", title=title, facet_col=facet_col
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
        return fig

    def breed_pie(self, title: str):
        target_col = "animal_Variety_converted"
        count_df = self.groupby_count_preprocess(target_col)
        fig = px.pie(
            count_df,
            names=target_col,
            values="Count",
            title=title,
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        return fig

    def breed_exclude_mix(self, title: str):
        target_col = "animal_Variety_converted"
        count_df = self.groupby_count_preprocess(
            target_col, query=f"{target_col} != '米克斯'"
        )
        count_df = count_df.sort_values(by="Count")
        fig = px.bar(
            count_df,
            y=target_col,
            x="Count",
            title=title,
            orientation="h",
            height=900,
            text_auto=True,
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        return fig

    def age_pie(self, title: str):
        target_col = "animal_age"
        count_df = self.groupby_count_preprocess(target_col)
        fig = px.pie(
            count_df,
            names=target_col,
            values="Count",
            title=title,
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        return fig

    def age_bodytype_pie(self, title: str):
        target_col = "animal_age"
        facet_col = "animal_bodytype"
        count_df = self.groupby_count_preprocess([target_col, facet_col])
        fig = px.pie(
            count_df, names=target_col, values="Count", title=title, facet_col=facet_col
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
        return fig

    def colour_pie(self, title: str):
        target_col = "animal_colour"
        count_df = self.groupby_count_preprocess(target_col)
        fig = px.pie(
            count_df,
            names=target_col,
            values="Count",
            title=title,
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        return fig
