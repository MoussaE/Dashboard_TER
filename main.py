import dash
import dash_core_components as dcc
import dash_html_components as html
import os 
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from views.header import header 
from views.index import index
from dash.dependencies import Input, Output
from data.fetcher import fetcher 


app = dash.Dash(__name__)

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/map':
        return html.Div(children= "1")
    elif pathname == '/plot':
        return html.Div(children= "2")
    else:
        return index


if __name__ == '__main__':
   
    app.layout = html.Div([dcc.Location(id='url', refresh=False) ,header , html.Div(id='page-content', children=[]) , header])    
    app.run_server(debug=True)