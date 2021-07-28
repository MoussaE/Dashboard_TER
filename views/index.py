import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc
import os
import json
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from data.fetcher import fetcher
from views.header import header
from views.footer import footer

f = fetcher()

df = pd.read_sql("select  t.table_name as Table,d.description, c.reltuples as Tuples, c.relpages*8192 as taille , tst.ts as Modifie \
  from information_schema.tables t left join public.timestamps tst on t.table_name = BTRIM(tst.table_name, '()') , pg_class c left join  pg_description d on c.oid = d.objoid \
  where t.table_name = c.relname \
  and  t.table_schema = 'public'  \
  and  t.table_catalog = 'piratage' and t.table_name <> 'timestamps' ;", f.cnt.conn)


index = html.Div(
    className="schema_chart",
    children=[
        
        dbc.Row(dbc.Col(header)),
        dbc.Row(dbc.Col(
            dbc.Jumbotron([
                dbc.Container(
                    [
                        
                        html.H1(
                            "Base de données sur le piratage de logiciels", className="display-3"),
                        html.P(
                            "L’objectif du projet consistera à observer et formuler des hypothèses explicatives de l’évolution du cybercrime. Nous nous focaliserons sur une forme particulière de cette criminalité : le piratage de logiciels. Le cybercrime est une catégorie de crime assez large, dont les formes ou modalités particulières sont nombreuses. Nous englobons dans cette catégorie les actes criminels en ligne et hors ligne, dès lors qu’ils mobilisent des moyens informatiques. Le « piratage de logiciel » est l’un des formes de la criminalité informatique. En termes juridiques elle est qualifiée de « contrefaçon » (toute forme d’atteinte à la propriété intellectuelle des logiciels, ie. copie sans autorisation, modifications illicites du code, utilisation sans licence, distribution non autorisée...)."
                            "Cette base de donnée contient toutes les informations regroupés dans le cadre de l'étude sur l'évolution du cyber-crime",
                            className="lead",
                        ),
                        html.P(
                            "Une description des tables, ainsi que plusieurs moyens de visualisation son mis à disposition de l'utilisateur",
                            className="lead",
                        ),
                    ],
                    fluid=False,
                )
            ],
                fluid=False,
            ))),
        dbc.Row(dbc.Col(html.H1(
            children='Informations sur les tables',
            id='title-metadata',
        ))),
        dbc.Row(dbc.Col(dash_table.DataTable(id="metadata",
                                             columns=[{"name": i, "id": i}
                                                      for i in df.columns],
                                             data=df.to_dict('records'),
                                             ))),
        dbc.Row(dbc.Col(html.H1(
            children='Visualiastion des données',
            id='visualisation',
        ))),
        dbc.Row(
            [
                dbc.Col(dbc.Card(
                    [
                        dbc.CardImg(src="/assets/map.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Cartes", className="card-title"),
                                html.P(
                                    "Visualisation des données cartographiques",
                                    className="card-text",
                                ),
                                dbc.Button("Visualiser", color="primary",href="/map"),
                            ]
                        ),
                    ],
                    style={"width": "18rem", "offset": "3"},
                ), align="start"),
                dbc.Col(html.Div(dbc.Card(
                    [
                        dbc.CardImg(src="/assets/map.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Graphiques", className="card-title"),
                                html.P(
                                    "Visualisation des données sous formes de graphiques",
                                    className="card-text",
                                ),
                                dbc.Button("Visualiser", color="primary", href="/plot"),
                            ]
                        ),
                    ],
                    style={"width": "18rem"},
                )), align="end"),
                 dbc.Col(dbc.Card(
                    [
                        dbc.CardImg(src="/assets/map.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Comparatifs", className="card-title"),
                                html.P(
                                    "Comparaisons entre differentes valeurs",
                                    className="card-text",
                                ),
                                dbc.Button("Visualiser", color="primary",href="/compare"),
                            ]
                        ),
                    ],
                    style={"width": "18rem", "offset": "3"},
                ), align="center")
            ]
        ),
        dbc.Row(dbc.Col(footer))
    ]
)
