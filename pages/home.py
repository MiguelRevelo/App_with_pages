import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div(
    [
        html.Div(
            [
                html.H1("Fitness Tracker", className="home-title"),
                html.P("Your fitness journey starts here!", className="home-subtitle"),
            ],
            className="text-container",
        )
    ],
    className="home-container",
)
