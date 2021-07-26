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
        self.categories_pays = self.query["country"].keys()
        self.recup = fetcher ()
        
      
        
    def draw_func (self , table_name , world = False, country_name = "" , year = 1990):
        
        self.countries = pd.read_sql_query("select distinct ( nicename ) , iso from countries order by  nicename ; ", self.recup.cnt.conn )
        
     
        self.years = pd.read_sql_query("select  distinct (year) from " +self.query["rename"][table_name]  +" ;" , self.recup.cnt.conn )
      
        if  not world :
            
            requete  = self.query["country"][table_name] + "\'"+ str (country_name) + "\';"
            query = "select distinct ( nicename )  from countries where  nicename not in (select  nicename from "+ self.query["rename"][table_name]  +"  where countries.id =  "+self.query["rename"][table_name]  +".country_id   ) ; "
            self.countriesNotIn = pd.read_sql_query(query, self.recup.cnt.conn )
            print(query)
            layout = go.Layout(title="", height=600, width=800)
            df  = self.recup.get_data (requete)
            fig = go.Figure([go.Bar(x=df["Year"], y=df["Value"],  marker_color="#A77B93")], layout=layout)
            return fig 
        else : 
            #recup les  coordonnees 
            datatmp = px.data.gapminder().query("year==2007")
            requete = self.query["world"][table_name ] +  str (year) + ";"
            self.countriesNotIn = pd.read_sql_query("select distinct ( nicename )  from countries where  nicename not in (select  nicename from "+ self.query["rename"][table_name]  +"  where countries.id =  "+self.query["rename"][table_name]  +".country_id  and "+  self.query["rename"][table_name]+".year = "+str (year)+"  ) ; ", self.recup.cnt.conn )
         
            df= self.recup.get_data (requete , True) ; 
            dataframe_merge = pd.merge(df,datatmp , left_on = ['CountryName'], right_on = ['country'])
            fig = px.choropleth(dataframe_merge , locations="iso_alpha",color="Value", hover_name="country",color_continuous_scale=px.colors.sequential.Plasma)
            return fig 


    def draw_compare(self , country_name_1 , country_name_2 , table ):
        fig = go.Figure()
     
        self.countries = pd.read_sql_query("select distinct ( nicename ) , iso from countries order by  nicename ; ", self.recup.cnt.conn )
        self.countriesNotIn = pd.read_sql_query("select distinct ( nicename )  from countries where  nicename not in (select  nicename from "+ self.query["rename"][table]  +"  where countries.id =  "+self.query["rename"][table]  +".country_id   ) ; ", self.recup.cnt.conn )
     
        requete  = self.query["country"][table] + "\'"+ str (country_name_1) + "\';"
        df  = self.recup.get_data (requete)
        
        requete1  = self.query["country"][table] + "\'"+ str (country_name_2) + "\';"
        df2  = self.recup.get_data (requete1)
        name_1 = str (table) +"("+ str ( country_name_1) +")"
        name_2 = str (table) +"("+ str (country_name_2) +")"

        if df.empty:
            name_1 = "pas de donnees (vide)"
        if df2.empty: 
            name_2 = "pas de donnees (vide)"
        
        fig.add_trace(go.Scatter(x=df2["Year"], y=df2["Value"], mode='markers',name= name_2))
        fig.add_trace(go.Scatter(x=df["Year"],  y=df["Value"] , mode='markers' ,name=name_1))


        return fig
