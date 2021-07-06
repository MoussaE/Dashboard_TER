import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import os 
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from data.fetcher import fetcher

f = fetcher()

df = pd.read_sql("select  t.table_name as Table,d.description, c.reltuples as Tuples, c.relpages*8192 as taille , tst.ts as Modifie \
  from information_schema.tables t left join public.timestamps tst on t.table_name = BTRIM(tst.table_name, '()') , pg_class c left join  pg_description d on c.oid = d.objoid \
  where t.table_name = c.relname \
  and  t.table_schema = 'public'  \
  and  t.table_catalog = 'piratage' and t.table_name <> 'timestamps' ;", f.cnt.conn)


index = html.Div([
    html.H1(
        children='Informations sur les table',
        id='title-metadata',
    ),
    dash_table.DataTable(id="metadata",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    html.H1(
        children='Visualiastion des données',
        id='visualisation',
    ),
])
