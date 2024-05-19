import dash
from dash import Input, Output, callback, dcc, html

from functions.callbacks import register_callbacks

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("Live Data", className="live-header-title"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.H2("Heart Rate", className="pulse-title"),
                                html.Div(id="pulseid", className="pulse-value"),
                            ],
                            className="pulse-container",
                        ),
                        html.Div(
                            [
                                html.H2("Oximeter", className="oximeter-title"),
                                html.Div(id="oximeterid", className="oximeter-value"),
                            ],
                            className="oximeter-container",
                        ),
                    ],
                    className="pulse-oximeter",
                ),
                html.Div(
                    [
                        dcc.Graph(id="plotid", className="live-graph"),
                        dcc.Interval(
                            id="interval-component", interval=1000, n_intervals=0
                        ),
                    ],
                    className="live-graph-container",
                ),
            ],
            className="live-middle",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Calories Burned", className="calories-title"),
                        html.Div("100", className="calories-value"),
                    ],
                    className="calories-container",
                ),
                html.Div(
                    [
                        html.H2("Steps", className="steps-title"),
                        html.Div("500", className="steps-value"),
                    ],
                    className="steps-container",
                ),
                html.Div(
                    [
                        html.H2("Distance", className="distance-title"),
                        html.Div("0.5", className="distance-value"),
                    ],
                    className="distance-container",
                ),
                html.Div(
                    [
                        html.H2("Active Minutes", className="active-title"),
                        html.Div("30", className="active-value"),
                    ],
                    className="active-container",
                ),
            ],
            className="live-bottom",
        ),
    ],
    className="live-container",
)
