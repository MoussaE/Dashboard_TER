import dash
import dash_core_components as dcc
import dash_html_components as html
import os 
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from views.header import header 

from views.footer import footer
from views.index import index
from dash.dependencies import Input, Output
from data.fetcher import fetcher 
from views.affichage import * 


app = dash.Dash(__name__ ,suppress_callback_exceptions=True)

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')]  )
def display_page(pathname):
    if pathname == '/map':
        return html.Div([corps_map])
    elif pathname == '/plot':
        return html.Div([corps_plot])
    else:
        return index



@app.callback( Output('graph_map', 'figure'),Input('drop_tables_map', 'value') , Input('year-slider', 'value')  )
def update_figure(selected_table , selected_year):
    print(selected_year)
    fig = dessinateur.draw_func ( selected_table ,  True  , year =selected_year) 
    fig.update_layout(transition_duration=500)
    return fig


@app.callback( Output('graph_plot', 'figure'), Input('drop_tables', 'value') , Input('drop_countries', 'value')  )
def update_figure(selected_table , selected_country):
    print(selected_country)
    fig = dessinateur.draw_func (selected_table ,  False   , selected_country ) 
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':
    app.layout = html.Div([dcc.Location(id='url', refresh=False) ,header , html.Div(id='page-content', children=[]) , header])    
    app.run_server(debug=True)
