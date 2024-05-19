import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("This is our ai-assistance page"),
        html.Div("This page will contain our ai features"),
    ]
)
