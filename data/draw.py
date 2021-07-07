import dash
import dash_core_components as dcc
import dash_html_components as html
import os 
import json
import plotly.graph_objects as go
import pandas as pd 
import plotly.express as px
from data.fetcher import fetcher


class  draw: 
    def __init__(self) -> None:
      
        with open(os.getcwd() + "/config/" +  "query.json", "r") as read_file:
            self.query = json.load(read_file)
        self.categories = self.query["world"].keys()
        print (self.categories)
        self.recup = fetcher ()
        
      
        
    def draw_func (self , table_name , world = False, country_name = "" , year = 1990):
        self.countries = pd.read_sql_query("select distinct ( nicename ) , iso from countries ,  "+self.query["rename"][table_name] +  " where countries.id =  " + 
        self.query["rename"][table_name]+".country_id ;", self.recup.cnt.conn )

        self.years = pd.read_sql_query("select  distinct (year) from " +self.query["rename"][table_name]  +" ;" , self.recup.cnt.conn )
        if  not world :
            requete  = self.query["country"][table_name] + "\'"+ str (country_name) + "\';"
            print(requete)
            df  = self.recup.get_data (requete)
            fig = go.Figure([go.Bar( x=df["Year"], y=df["Value"] ,  marker_color="orange")]) 
            return fig 
        else : 
            datatmp = px.data.gapminder().query("year==2007")
            requete = self.query["world"][table_name ] +  str (year) + ";"
            print(requete)
            df= self.recup.get_data (requete , True) ; 
            dataframe_merge = pd.merge(df,datatmp , left_on = ['CountryName'], right_on = ['country'])
            fig = px.choropleth(dataframe_merge , locations="iso_alpha",color="Value", hover_name="country",color_continuous_scale=px.colors.sequential.Plasma)
            return fig 


    def draw_compare(self , country_name , tb_1 , tb_2 ):
        fig = go.Figure()
     
        self.countries = pd.read_sql_query("select distinct ( nicename ) , iso from countries", self.recup.cnt.conn )
        self.categories_pays = self.query["country"].keys()

        requete  = self.query["country"][tb_1] + "\'"+ str (country_name) + "\';"
        df  = self.recup.get_data (requete)
        
        requete1  = self.query["country"][tb_2] + "\'"+ str (country_name) + "\';"
        df2  = self.recup.get_data (requete1)
        
        fig.add_trace(go.Scatter(x=df2["Year"], y=df2["Value"], mode='markers',name= tb_2))
        fig.add_trace(go.Scatter(x=df["Year"], y=df["Value"], mode='markers',name= tb_1))


        return fig
