import dash
from dash import Dash

from functions.acceso import accesos
from functions.app_layout import app_layout
from functions.links_callbacks import links_callbacks
from functions.live_data_callbacks import Live_plot
from functions.start_stop import start_stop_callbacks

ref = accesos()

app = Dash(__name__, use_pages=True)

app.layout = app_layout()

links_callbacks(app)

Live_plot(app, ref)

start_stop_callbacks(app, ref)

if __name__ == "__main__":
    app.run(debug=True)
