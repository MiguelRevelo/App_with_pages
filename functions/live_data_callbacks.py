import plotly
from dash import Input, Output, html


def Live_plot(app, ref):

    @app.callback(
        Output("pulseid", "children"),
        Output("oximeterid", "children"),
        Input("interval-component", "n_intervals"),
    )
    def update_metrics(n):
        try:
            pulse = ref.get()["pulse"]
            ox = ref.get()["oximeter"]
            return [
                html.Span(" {}".format(pulse[-1])),
                html.Span(" {}".format(ox[-1])),
            ]
        except Exception as e:
            return [html.Span("N/A"), html.Span("N/A")]

    @app.callback(
        Output("plotid", "figure"),
        Input("interval-component", "n_intervals"),
    )
    def update_graph_live(n):
        try:
            x = ref.get()["x"]
            y = ref.get()["y"]
            data = plotly.graph_objs.Scatter(
                x=x,
                y=y,
                name="Scatter",
                mode="lines+markers",
            )

            return {
                "data": [data],
                "layout": plotly.graph_objs.Layout(
                    xaxis=dict(range=[min(x), max(x)]),
                    yaxis=dict(range=[min(y), max(y)]),
                    margin=dict(l=25, r=25, t=30, b=25),
                    title=("Live data plot"),
                ),
            }
        except Exception as e:
            return {
                "data": [],
                "layout": plotly.graph_objs.Layout(title="Error loading data"),
            }
