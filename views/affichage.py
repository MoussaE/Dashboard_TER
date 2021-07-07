import dash
import dash_core_components as dcc
import dash_html_components as html
import os 
import json
from dash_html_components.Br import Br
from dash_html_components.Header import Header
from numpy.lib.function_base import median
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from data.Connector import Connector 
from data.draw import draw 
from dash.dependencies import Input, Output
from views.header import header 

dessinateur = draw()
nom_table = "population par pays"
figure_plot= dessinateur.draw_func ( nom_table , False   , "France" , year = 2010) 
figure_map = dessinateur.draw_func ( nom_table , True   , "France" , year = 2010) 
 
marks = { x  : str (x) for  x in range (1990 , 2021)}


#monde 
corps_map = html.Div([
    header,
    dcc.Graph(id='graph_map',figure=figure_map,),
    dcc.Dropdown( 
                            options=[ {'label': value   ,'value': value } for  value  in dessinateur.categories ],
                            multi=False,
                            value= nom_table ,
                            placeholder= "Données",
                            id = "drop_tables_map",
                            className="schema_chart"
            
                      ),
         
         html.Br(children=[]),
         html.Br(children=[]), 
    html.Div(
        [ 
            html.Br(children=[]), 
            html.Div([dcc.Slider( step = 1 ,marks=  marks , min = 1990 , max = 2020 , value = 2010 , included=False, id = "year-slider" )]),
    
        ],style={'text-align': 'center'}),
])

#pays 

corps_plot= html.Div([

    dcc.Graph(id='graph_plot',figure=figure_plot,),
    html.Div(
        [ 

        header,
        dcc.Dropdown( 
                            options=[ {'label': value   ,'value': value } for  value  in dessinateur.categories ],
                            multi=False,
                            value= nom_table ,
                            placeholder= "Données",
                            id = "drop_tables"
            
                      ),
         
         html.Br(children=[]), 
         html.Br(children=[]), 
         dcc.Dropdown( 
                            options=[ {'label': value ["nicename"]  ,'value': value["nicename"] } for  key , value  in dessinateur.countries.iterrows() ],
                            multi=False,
                            value= dessinateur.countries["nicename"][0],
                            placeholder= "Nom pays",
                            id = "drop_countries"
            
                      ),
       
            html.Br(children=[]), 
            html.Br(children=[]), 
    
        ],style={'text-align': 'center'}),
])



