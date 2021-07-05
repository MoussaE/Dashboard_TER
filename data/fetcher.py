import os 
import json
import plotly.graph_objects as go
import pandas as pd 
from data.Connector import Connector 
import plotly.express as px



class fetcher:
    def __init__(self) -> None:
        path  = os.getcwd() + "/config/" +  "config.json"
        with open(path, "r") as read_file:
            config = json.load(read_file)
        self.cnt = Connector(config["param"]["user"], config["param"]["host"], config["param"]["mdp"], config["param"]["port"], config["param"]["db"])
        self.cur = self.cnt.connect()
        self.cnt.conn.autocommit = True


    def get_data(self , query , world = False):
        self.cur.execute (query)
        df = self.cur.fetchall()
        
        if  not world : 
            df = pd.DataFrame(df ,columns=["CountryName" , "Value" , "Year"])
        else :
            df  = pd.DataFrame(df ,columns=["CountryName" , "iso" , "value"])
        return df 
