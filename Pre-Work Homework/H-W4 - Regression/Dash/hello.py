from dash import Dash, dcc
import dash_bootstrap_components as dbc

# build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
mytext = dcc.Markdown(children='# Hello World!')

# Layout
app.layout = dbc.Container([mytext])

# run app
if __name__ == '__main__':
    app.run_server(debug=True)
