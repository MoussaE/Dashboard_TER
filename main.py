import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import os
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
import imageio
from datetime import date
from views.header import header 
from dash.dependencies import Input, Output, State
from data.fetcher import fetcher 
from views.affichage import * 
from views.index import index


app = dash.Dash(__name__ ,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.LUX] )
server = app.server
app.layout = html.Div([dcc.Location(id='url', refresh=True), html.Div(id='page-content', children=[])])

@app.callback(Output('page-content', 'children'),[Input('url', 'pathname')]  )
def display_page(pathname):
    if pathname == '/map':
        return html.Div([corps_map])
    elif pathname == '/plot':
        return html.Div([corps_plot])
    elif pathname == "/compare":
        return html.Div([corps_compare])
    elif pathname == "/jupyter":
        return html.Div([corps_jupyter])
    else: 
        return index


@app.callback(Output('download-gif', 'data'), Input('gif_downloader', 'n_clicks'), State('drop_tables_map', 'value')) 
def download_gif(n_clicks, selected_table):
    current = os.getcwd()
    table_name = dessinateur.query["rename"][str(selected_table)] + str(date.today())
    if n_clicks:
        filenames = []
        images= []
        gifname = current + "/bin/gif/" + table_name +".gif"
        for year in range(2000, 2020):
            #print(year)
            fig = dessinateur.draw_func(selected_table, True, year=year)
            filename= current + "/bin/tmp/figure" + str(year) +".png"
            fig.write_image(filename)
            images.append(imageio.imread(filename))
            filenames.append(filename)
        imageio.mimsave(gifname, images,fps=4000)
        for filename in filenames:
            os.remove(filename)
        return dcc.send_file(gifname)

    




@app.callback( Output('graph_map', 'figure'),Input('drop_tables_map', 'value') , Input('year-slider', 'value'))
def update_figure(selected_table , selected_year):
    fig = dessinateur.draw_func ( selected_table ,  True  , year =selected_year) 
    fig.update_layout(transition_duration=500)
    return fig


@app.callback( Output('graph_plot', 'figure')
,Input('drop_tables', 'value')
,Input('drop_countries', 'value'))
def update_figure(selected_table , selected_country):
    fig = dessinateur.draw_func (selected_table ,  False   , selected_country ) 
    fig.update_layout(transition_duration=500)
    return fig


@app.callback( Output('graph_compare', 'figure')
,Input('drop_data_compare_1','value') 
,Input('drop_data_compare_2','value')
,Input('drop_tables2_compare','value')
)
def update_figure(country_1 ,country_2 , table):
    fig = dessinateur.draw_compare (country_1 ,country_2 , table)
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':   
    app.run_server(debug=False)
    
  