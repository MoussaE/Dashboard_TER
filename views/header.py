import dash
import dash_core_components as dcc
import dash_html_components as html
import os 
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px



# Conteneur du menu
header = html.Div(
                className="Header", 
                children=[html.Header(
                                    className="header",
                                    children=[
                                        #Bannière si pas besoin juste mette 'display:none'
                                        html.Div(
                                                className="header banner",
                                        ),
                                        #menu avec les liens 
                                        html.Div(
                                                className="header menu",
                                                children=[
                                                    html.Div(
                                                        className='logo_uvsq',
                                                        children=[
                                                            html.Img(
                                                                src="/assets/icon/logo-UVSQ-color.svg",
                                                                alt="Logo de l'université de Versailles"
                                                            )
                                                        ]
                                                    ),
                                                    html.Nav(
                                                        className="header menu nav",
                                                        children=[
                                                            html.Ul(
                                                                className="header menu nav-ul",
                                                                children=[
                                                                    html.Li(
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/house_purple.svg",
                                                                                        alt="logo maison"
                                                                                    )
                                                                                ],
                                                                                id="Accueil",
                                                                                href="#")
                                                                        ]),
                                                                    html.Li(
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/chart.svg",
                                                                                        alt="logo maison"
                                                                                    )
                                                                                ],
                                                                                id="Graphique",
                                                                                href="#")
                                                                        ]),
                                                                    html.Li(
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/python_fill_purple.svg",
                                                                                        alt="logo maison"
                                                                                    )
                                                                                ],
                                                                                id="Jupyter-Notebook",
                                                                                href="#")
                                                                        ])
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="logo_github",
                                                        children=[
                                                            html.A(
                                                                children=[
                                                                    html.Img(
                                                                        src="/assets/icon/github_purple.svg",
                                                                        alt="logo github"
                                                                    )
                                                                ],
                                                                id="Github",
                                                                href="#"
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        
                                    ]
                            )
                        ]
        )

