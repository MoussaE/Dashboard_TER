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
                                                            html.A (
                                                                children=[
                                                                    html.Img(
                                                                        src="/assets/icon/uvsq_ufr.svg",
                                                                        alt="Logo de l'université de Versailles"
                                                                    )
                                                                ],
                                                                className="logo_lien",
                                                                href="https://www.uvsq.fr/"
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
                                                                                href="/")
                                                                        ]),
                                                                    html.Li(
                                                                        id="remove-graphique",
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/chart.svg",
                                                                                        alt="logo graphique"
                                                                                    )
                                                                                ],
                                                                                id="Graphique",
                                                                                href="/plot")
                                                                        ]),
                                                                    html.Li(
                                                                        id="remove-globe",
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/globe.svg",
                                                                                        alt="logo globe terrestre"                                                                                    )
                                                                                ],
                                                                                id="Globe",
                                                                                href="/map")
                                                                        ]),
                                                                    html.Li(
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/python_fill_purple.svg",
                                                                                        alt="logo Python"
                                                                                    )
                                                                                ],
                                                                                id="Jupyter-Notebook",
                                                                                href="http://192.168.33.56:8888/?token=12d1a9ff71ddd4e9db81369e4fd042f8098e0d8438280502"
                                                                            )
                                                                        ]),
                                                                    html.Li(
                                                                        className="header menu nav-ul nav-ul--li",
                                                                        children=[
                                                                            html.A(
                                                                                children=[
                                                                                    html.Img(
                                                                                        src="/assets/icon/compare.svg",
                                                                                        alt="logo comparaison de fichier"
                                                                                    )
                                                                                ],
                                                                                id="Compare",
                                                                                href="/compare")
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
                                                                        src="/assets/icon/github_white.svg",
                                                                        alt="logo github"
                                                                    )
                                                                ],
                                                                id="Github",
                                                                href="https://github.com/piratage-ter"
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        
                                    ]
                            )
                        ]
        )
