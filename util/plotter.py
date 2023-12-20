import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


class DogDataPlotter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def yearly_plot(self):
        year_groupby = self.df.groupby("year", as_index=False).count()
        fig = px.bar(
            year_groupby,
            x="year",
            y="animal_id",
            title="每年分佈",
            # height=400,
            text_auto=True,
        )
        fig.update_traces(showlegend=False)
        fig.update_xaxes(dtick=1)
        return fig

    def monthly_plot(self):
        month_groupby = self.df.groupby("month", as_index=False).count()
        fig = px.bar(
            month_groupby, x="month", y="animal_id", title="每月分佈", text_auto=True
        )
        fig.update_xaxes(dtick=1)
        return fig

    def multi_yearly_plot(self):
        year_groupby = self.df.groupby(["year", "month"], as_index=False).count()
        year_range = list(range(2020, 2024))
        fig = px.bar(
            year_groupby.query(f"year in {year_range}"),
            x="month",
            y="animal_id",
            color="animal_id",
            facet_row="year",
            facet_row_spacing=0,
            text_auto=True,
        )
        fig.update_layout(height=600, title_text="2020 ~ 2023年每月分佈")
        fig.update_xaxes(dtick=1)
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
        return fig

    def draw_pie(
        self,
        target_col: str,
        title: str,
        facet_col: str = None,
        facet_row: str = None,
        width: int = 600,
        textfont_size: int = 24,
        color_by_target_col: bool = True,
    ):
        if facet_col or facet_row:
            if facet_col:
                groupby_cols = [target_col, facet_col]
            else:
                groupby_cols = [target_col, facet_row]
        else:
            groupby_cols = target_col

        tmp_groupby_df = self.df.groupby(groupby_cols, as_index=False).count()
        if color_by_target_col:
            fig = px.pie(
                tmp_groupby_df,
                names=target_col,
                values="animal_id",
                facet_col=facet_col,
                facet_row=facet_row,
                title=title,
                width=width,
                color=target_col,
            )
        else:
            fig = px.pie(
                tmp_groupby_df,
                names=target_col,
                values="animal_id",
                facet_col=facet_col,
                facet_row=facet_row,
                title=title,
                width=width,
            )
        fig.update_traces(textposition="inside", textfont_size=textfont_size)
        if facet_col or facet_row:
            fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))
            # fig.for_each_trace(lambda t: t.update(name=t.name.split("=")[1]))
        return fig

    def dog_breed_exclude_mix(self):
        animal_Variety_exclude_mix = (
            self.df.query("animal_Variety_converted != '米克斯'")
            .groupby("animal_Variety_converted", as_index=False)
            .count()
        )
        animal_Variety_exclude_mix = animal_Variety_exclude_mix.sort_values(
            by="animal_id"
        )
        fig = px.bar(
            data_frame=animal_Variety_exclude_mix,
            y="animal_Variety_converted",
            x="animal_id",
            title="品種比例（不含米克斯）",
            orientation="h",
            height=900,
            text_auto=True,
        )
        fig.update_traces(textposition="inside", textfont_size=24)
        return fig
