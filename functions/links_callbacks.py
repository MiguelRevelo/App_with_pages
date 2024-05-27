from dash import Input, Output, html


def links_callbacks(app):
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
            (
                "exercises-link active-link"
                if pathname == "/exercises"
                else "exercises-link"
            ),
            "test-link active-link" if pathname == "/test" else "test-link",
            (
                "ai-assistance-link active-link"
                if pathname == "/ai-assistance"
                else "ai-assistance-link"
            ),
        ]
