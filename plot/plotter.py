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
        return fig
