from dash import Input, Output, html


def start_stop_callbacks(app, ref):
    @app.callback(Output("start-button", "n_clicks"), Input("start-button", "n_clicks"))
    def start_button(n_clicks):
        if n_clicks is not None:
            ref.update({"bool": True})
            return n_clicks

    @app.callback(Output("stop-button", "n_clicks"), Input("stop-button", "n_clicks"))
    def stop_button(n_clicks):
        if n_clicks is not None:
            ref.update({"bool": False})
            return n_clicks
