import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html

from functions.callbacks import register_callbacks

app = Dash(__name__, use_pages=True)

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Location(id="url", refresh=False),
                html.H2("Fitness Tracker", className="header-title"),
                html.Div(
                    [
                        dcc.Link(
                            "Home", href="/", className="home-link", id="home-link"
                        ),
                        dcc.Link(
                            "About",
                            href="/about",
                            className="about-link",
                            id="about-link",
                        ),
                        dcc.Link(
                            "Recommendations",
                            href="/recommendations",
                            className="recommendations-link",
                            id="recommendations-link",
                        ),
                        dcc.Link(
                            "Live Data",
                            href="/live-data",
                            className="live-link",
                            id="live-link",
                        ),
                        dcc.Link(
                            "Statistics",
                            href="/statistics",
                            className="statistics-link",
                            id="statistics-link",
                        ),
                        dcc.Link(
                            "Exercises",
                            href="/exercises",
                            className="exercises-link",
                            id="exercises-link",
                        ),
                        dcc.Link(
                            "Test", href="/test", className="test-link", id="test-link"
                        ),
                        dcc.Link(
                            "AI Assistance",
                            href="/ai-assistance",
                            className="ai-assistance-link",
                            id="ai-assistance-link",
                        ),
                    ],
                    className="menu-items",
                ),
            ],
            className="menu",
        ),
        html.Div(dash.page_container, className="content"),
    ],
    className="container",
)


@app.callback(
    [
        Output("home-link", "className"),
        Output("about-link", "className"),
        Output("recommendations-link", "className"),
        Output("live-link", "className"),
        Output("statistics-link", "className"),
        Output("exercises-link", "className"),
        Output("test-link", "className"),
        Output("ai-assistance-link", "className"),
    ],
    [Input("url", "pathname")],
)
def update_active_link(pathname):
    active_class = "active-link"
    return [
        "home-link active-link" if pathname == "/" else "home-link",
        "about-link active-link" if pathname == "/about" else "about-link",
        (
            "recommendations-link active-link"
            if pathname == "/recommendations"
            else "recommendations-link"
        ),
        "live-link active-link" if pathname == "/live-data" else "live-link",
        (
            "statistics-link active-link"
            if pathname == "/statistics"
            else "statistics-link"
        ),
        "exercises-link active-link" if pathname == "/exercises" else "exercises-link",
        "test-link active-link" if pathname == "/test" else "test-link",
        (
            "ai-assistance-link active-link"
            if pathname == "/ai-assistance"
            else "ai-assistance-link"
        ),
    ]


register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
