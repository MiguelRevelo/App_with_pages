import dash
from dash import dcc, html


def app_layout():
    return html.Div(
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
                                "Test",
                                href="/test",
                                className="test-link",
                                id="test-link",
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
