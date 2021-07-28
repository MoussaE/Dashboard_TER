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
from views.footer import footer

dessinateur = draw()
nom_table = "population par pays"
figure_plot= dessinateur.draw_func ( nom_table , False   , "France" , year = 2010) 
figure_map = dessinateur.draw_func ( nom_table , True   , "France" , year = 2010) 
figure_compare = dessinateur.draw_compare("Argentina" , nom_table , nom_table )
 
marks = { x  : str (x) for  x in range (1990 , 2021)}


#monde 
corps_map = html.Div(
    className="schema_chart", 
    children=[
    header,
    dcc.Graph(id='graph_map',figure=figure_map,),
    dcc.Dropdown( 
                            options=[ {'label': value   ,'value': value } for  value  in dessinateur.categories ],
                            multi=False,
                            value= nom_table ,
                            placeholder= "Données",
                            id = "drop_tables_map",
                            className="menu-deroulant"
                      ),
         
         html.Br(children=[]),
         html.Br(children=[]), 
    html.Div(
        [ 
            html.Br(children=[]), 
            dcc.Dropdown(
                options=[{'label': value, 'value': value}
                         for value in marks],
                multi=False,
                value=2000,
                placeholder="Données",
                id="year-slider",
                className="menu-deroulant"

            )
        ],style={'text-align': 'center'}),
        footer
])

#pays 
corps_plot= html.Div(
    className="schema_chart",
    children=[
    html.Div(
        [ 
        header,
        dcc.Graph(id='graph_plot', figure=figure_plot,),
        dcc.Dropdown( 
                            options=[ {'label': value   ,'value': value } for  value  in dessinateur.categories_pays ],
                            multi=False,
                            value= nom_table ,
                            placeholder= "Données",
                            id="drop_tables",
                            className="menu-deroulant"
            
                      ),
         
         html.Br(children=[]), 
         html.Br(children=[]), 
         dcc.Dropdown( 
                            options=[],
                            multi=False,
                            value= dessinateur.countries["nicename"][0],
                            placeholder= "Nom pays",
                            id = "drop_countries",
                            className="menu-deroulant"
            
                      ),
       
            html.Br(children=[]), 
            html.Br(children=[]), 
    
        ],style={'text-align': 'center'}),
        footer
])


corps_jupyter= html.Div(
    className="schema_chart",
    children=[
        header,
        html.Div(
            id="frame_jn",
            children = [
                html.Iframe(
                    src="https://192.168.33.56:8888"
                )
            ]
        ),
        footer
    ]
)


corps_compare= html.Div(
    className="schema_chart",
    children=[

    
    html.Div(
        className="schema_chart",
        children=[ 
        header,
        dcc.Graph(id='graph_compare', figure=figure_compare,),
        html.Br(children=[]), 
        dcc.Dropdown(     

                            options=[ {'label': value ["nicename"]  ,'value': value["nicename"] } for  key , value  in dessinateur.countries.iterrows() ],

                            multi=False,
                            value= dessinateur.countries["nicename"][0],
                            placeholder= "Nom pays",
                            id = "drop_data_compare_1",
                            className="menu-deroulant"
            
                      ),
       
            html.Br(children=[]),

         dcc.Dropdown( 
                            options=[ {'label': value ["nicename"]  ,'value': value["nicename"] } for  key , value  in dessinateur.countries.iterrows() ],
                            multi=False,
                            value= dessinateur.countries["nicename"][0],
                            placeholder= "Nom pays",
                            id = "drop_data_compare_2",
                            className="menu-deroulant"
            
                      ),
         
         html.Br(children=[]),  

          dcc.Dropdown( 
                            options=[ {'label': value   ,'value': value } for  value  in dessinateur.categories_pays ],
                            multi=False,
                            value= nom_table ,
                            id = "drop_tables2_compare",
                            className="menu-deroulant"
            
                      ),
         
         html.Br(children=[]), 

            html.Br(children=[]), 
    
        ],style={'text-align': 
        'center'}),
        footer
])
