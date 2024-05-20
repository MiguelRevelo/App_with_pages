import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    [
        html.H1("Routines and Exercises", className="exercises-title"),
        html.Div(
            [
                html.Div(
                    [
                        html.H2("For Men"),
                        html.Img(
                            src="/assets/workoutsformen.jpg", className="workout-image"
                        ),
                    ],
                    className="men-container",
                ),
                html.Div(
                    [
                        html.H2("For Women"),
                        html.Img(
                            src="/assets/workoutsforwomen.jpg",
                            className="workout-image",
                        ),
                    ],
                    className="women-container",
                ),
            ],
            className="men-women-container",
        ),
    ],
    className="exercises-container",
)
