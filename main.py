import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import os 
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from views.header import header 
from dash.dependencies import Input, Output
from data.fetcher import fetcher 
from views.affichage import * 
from views.index import index

app = dash.Dash(__name__ ,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.LUX] )

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')]  )
def display_page(pathname):
    if pathname == '/map':
        return html.Div([corps_map])
    elif pathname == '/plot':
        return html.Div([corps_plot])
    elif pathname == "/compare":
        return html.Div([corps_compare])
    else: 
        return index



@app.callback( Output('graph_map', 'figure'),Input('drop_tables_map', 'value') , Input('year-slider', 'value')  )
def update_figure(selected_table , selected_year):
    fig = dessinateur.draw_func ( selected_table ,  True  , year =selected_year) 
    fig.update_layout(transition_duration=500)
    return fig


@app.callback( Output('graph_plot', 'figure'), Input('drop_tables', 'value') , Input('drop_countries', 'value')  )
def update_figure(selected_table , selected_country):

    fig = dessinateur.draw_func (selected_table ,  False   , selected_country ) 
    fig.update_layout(transition_duration=500)
    return fig


@app.callback( Output('graph_compare', 'figure'),Input('drop_countries_compare', 'value') ,Input('drop_tables_compare', 'value'), Input('drop_tables2_compare', 'value')   )
def update_figure(country , tb1 , tb2):
    fig = dessinateur.draw_compare (country , tb1 , tb2)
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':   
    app.layout = html.Div([dcc.Location(id='url', refresh=True), html.Div(id='page-content', children=[])])
    app.run_server(debug=True)
  