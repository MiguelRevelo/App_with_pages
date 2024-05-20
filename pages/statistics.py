import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("This is our statistics page", className="statistics-title"),
        # Statistics related to fitness and excercise
        html.Div(
            [
                html.Div(
                    [
                        html.Div("Mean calories burned", className="mean-calories"),
                        html.Div("Mean steps taken", className="mean-steps"),
                    ],
                    className="calories-steps",
                ),
                html.Div(
                    [
                        html.Div("Mean sleep hours", className="mean-sleep"),
                        html.Div(
                            "air quality vs heart rate",
                            className="air-quality-vs-heart-rate",
                        ),
                    ],
                    className="sleep-air-quality",
                ),
            ],
            className="statistics-content",
        ),
    ],
    className="statistics-container",
)

"""
recomendations:
- gym routine
- diet
- sleep
- water intake
"""
