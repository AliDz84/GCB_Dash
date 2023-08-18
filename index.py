import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from flask import Flask
import sqlite3
import pandas as pd
from datetime import datetime

server=Flask(__name__)
app=dash.Dash(__name__,use_pages=True,server=server,external_stylesheets=[dbc.themes.SUPERHERO])
con = sqlite3.connect("assets/db.db")
data = pd.read_sql_query("SELECT * from general_info", con)
data_date=datetime.strptime(data.iloc[0, 1],'%Y-%m-%d %H:%M:%S')
data_date=data_date.strftime("%d-%m-%Y")
print(type(data_date))
sidebar=dbc.Nav(
    [
        dbc.NavLink(
            [
            html.Div(page["name"],className="lead"),
            ],
            href=page["path"],
            active="exact",
            )
        for page in dash.page_registry.values()
        ],
    vertical=True,
    pills=True,
    className="bg-Blue",
            )

app.layout=dbc.Container([

        dbc.Row(
        [
        dbc.Col([
            html.Img(src="assets/logo.jpg",className = 'left',style={'margin-top': '20px','margin-left':'20px'}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
                   
            sidebar
            ],xs=2,sm=2,md=2,lg=2,xl=2,xxl=2),
        dbc.Col(
                [
            dbc.Row(
                [           
            html.Div("CONSTRUCTION OF SEPARATION AND DECARBONATION UNITS AT ALRAR EPC2 LOT 1",
                        style={'frontsize':'30','textAlign':'center','color':'#ffffff','margin-top':'20px','background-color':'OrangeRed'}),
            html.Div("- DASHBOARD - Mise à jour: "+data_date,
                        style={'frontsize':'30','bold':'True','textAlign':'center','color':'#ffffff','background-color':'OrangeRed'}),
            html.Hr(),
                    ]),
            dbc.Row(
                [
                    dash.page_container
                    ],)
            ],xs=10,sm=10,md=10,lg=10,xl=10,xxl=10)
            ]
        ),
    ],fluid=True)  

if __name__ == '__main__':
    app.run_server()
