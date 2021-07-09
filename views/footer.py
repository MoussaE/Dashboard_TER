import dash
import dash_core_components as dcc
import dash_html_components as html
import os 
import json
from dash_html_components.H2 import H2
from dash_html_components.P import P
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
#<a target="_blank" href="https://icones8.fr/icon/DoB2hWAWiTer/graphique-combin%C3%A9">Graphique Combiné</a> icône par <a target="_blank" href="https://icones8.fr">Icons8</a>

footer = html.Footer(
                    className="Footer",
                    children= [
                        html.Div(
                            className="Copyright",
                            children= [
                                html.H2 (
                                   "Copyright",
                                    className="footer-h"
                                ),
                                html.P(
                                    children=[
                                        "Notre site utilise des icônes en provenance de ",
                                        html.A (
                                                "icones8.fr",
                                                href="https://www.icones8.fr"
                                        ),
                                        html.Br(),
                                        html.Img(
                                            src="/assets/icon/copyright.svg",
                                            alt="logo copyright"
                                        ),
                                        "Copyright 2021 - Laboratoire David, UFR Des Sciences de Versailles, UVSQ - Tous droits réservés"
                                    ]
                                )
                            ]
                                
                        ),
                        html.Div(
                            className="Contact",
                            children=[
                                html.H2 (
                                    "Contact",
                                    className="footer-h"
                                ),
                                html.P (
                                    children=[
                                        "Si vous souhaitez nous contacter, vous pouvez nous envoyer un email à ",
                                        html.A(
                                            "l'adresse suivante",
                                             href="mailto:wissam.serhan@ens.uvsq.fr;moussa.el-habar@ens.uvsq.fr;mohamed.debiane@ens.uvsq.fr"
                                        )
                                    ]
                                )
                                
                            ]
                        )
                    ]
            )

