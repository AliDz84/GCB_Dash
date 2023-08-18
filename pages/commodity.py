import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import sqlite3
import numpy as np

dash.register_page(__name__,name='Avancements des activités')
con = sqlite3.connect("assets/db.db")
data = pd.read_sql_query("SELECT * from commodity", con)
scope=pd.read_sql_query("SELECT * from scope", con)
fig = px.histogram(data,x='date', y=['Planifié','Réalisé'],barmode='group',
              title="")
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y",
    )
fig.update_yaxes(
    dtick="M1",
    tickformat="%b\n%Y",
    )
fig.update_layout(
    autosize=True,
    xaxis_title="Date",
    yaxis_title="Quantité",
    legend_title="Légende")

layout = html.Div(
    [
        dbc.Row(
            [               
             dbc.Col(
                    [
        dcc.Dropdown(options=['Quantités mensuelles', 'Quantités cumulées', 'Ecarts planning'],id='menu',value="Quantités mensuelles",style={'width':'90%'}),
                        ],
                    className='',
                    xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
        dbc.Col(
                    [
        dcc.Dropdown(options=[x for x in data.commodity.unique()],id='commodity-choice',value="Béton armé",style={'width':'90%'}),
                        ],
                    className='',
                    xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
             dbc.Col(
                    [
                        ],
                    className='',
                   xs=8,sm=8,md=8,lg=8,xl=8,xxl=8
                    ),
             html.Br(),
             html.Br(),
                html.Hr(),
                ]),
        dbc.Row(
            [               
                dbc.Col(
                    [
                dcc.Graph(id='graph',figure=fig)
                        ],
                    className='',
                    xs=12,sm=12,md=12,lg=12,xl=12,xxl=12
                    ),
                        ]),
        ])
@callback(
    Output('graph','figure'),
    Input('menu', 'value'),
    Input('commodity-choice', 'value')
)
def update_graph(value1,value2):
    if value1=="Quantités mensuelles":
        ts1 = data[data.commodity==value2]
        ts2 = scope[scope.commodity==value2]
        qty_totale="Qté totale= "+"{:.0f}".format(ts2['scope'].sum())+" "+str(ts2.iloc[0, 2])
        qty_actual="Qté réalisée= "+"{:.0f}".format(ts2['cum_actual'].sum())+" "+str(ts2.iloc[0, 2])
        qty_plan="Qté planifiée= "+"{:.0f}".format(ts2['cum_plan'].sum())+" "+str(ts2.iloc[0, 2])
        av="AV %= "+"{:.1%}".format(ts2['progress'].sum())
        var="Ecart planning= "+"{:.0f}".format(ts2['ecart_planning'].sum())+" "+str(ts2.iloc[0, 2])
        fig = px.histogram(ts1,x='date', y=['Planifié','Réalisé'],barmode='group', color_discrete_sequence=['orange','blue'],
        title=str(value2)+"   "+qty_totale+"   "+qty_plan+"   "+qty_actual+"   "+av+"   "+var,text_auto=True)
        fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",)
        fig.update_layout(
        autosize=True,
        xaxis_title="Date",
        yaxis_title="Quantité mensuelle ("+str(ts2.iloc[0, 2])+")",
        legend_title="Légende")
    if value1=="Quantités cumulées":
        ts1 = data[data.commodity==value2]
        ts2 = scope[scope.commodity==value2]
        qty_totale="Qté totale= "+"{:.0f}".format(ts2['scope'].sum())+" "+str(ts2.iloc[0, 2])
        qty_actual="Qté réalisée= "+"{:.0f}".format(ts2['cum_actual'].sum())+" "+str(ts2.iloc[0, 2])
        qty_plan="Qté planifiée= "+"{:.0f}".format(ts2['cum_plan'].sum())+" "+str(ts2.iloc[0, 2])
        av="AV %= "+"{:.1%}".format(ts2['progress'].sum())
        var="Ecart planning= "+"{:.0f}".format(ts2['ecart_planning'].sum())+" "+str(ts2.iloc[0, 2])
        trace_1 = go.Scatter(x=ts1['date'], y=ts1['Cum plan'], mode='lines', line=dict(color="orange"),name='Qty prévue')
        trace_2 = go.Scatter(x=ts1['date'], y=ts1['Cum actual'], mode='lines', line=dict(color="blue"),name='Qty réalisée')
        fig = go.Figure([
        trace_1, trace_2
        ])
        fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",)
        fig.update_layout(
        autosize=True,
        xaxis_title="Date",
        yaxis_title="Quantité cumulée ("+str(ts2.iloc[0, 2])+")",
        legend_title="Légende",
        title=str(value2)+"   "+qty_totale+"   "+qty_plan+"   "+qty_actual+"   "+av+"   "+var)
    if value1=="Ecarts planning":
        ts1 = data[data.commodity==value2]
        ts2 = scope[scope.commodity==value2]
        qty_totale="Qté totale= "+"{:.0f}".format(ts2['scope'].sum())+" "+str(ts2.iloc[0, 2])
        qty_actual="Qté réalisée= "+"{:.0f}".format(ts2['cum_actual'].sum())+" "+str(ts2.iloc[0, 2])
        qty_plan="Qté planifiée= "+"{:.0f}".format(ts2['cum_plan'].sum())+" "+str(ts2.iloc[0, 2])
        av="AV %= "+"{:.1%}".format(ts2['progress'].sum())
        var="Ecart planning= "+"{:.0f}".format(ts2['ecart_planning'].sum())+" "+str(ts2.iloc[0, 2])
        ts1["Color"] = np.where(ts1['Ecart']<0, 'red', 'green')
        fig = px.bar(ts1,x='date', y=['Ecart'],
        title=str(value2)+"   "+qty_totale+"   "+qty_plan+"   "+qty_actual+"   "+av+"   "+var)
        fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",)
        fig.update_traces(marker_color=ts1["Color"])
        fig.update_layout(
        autosize=True,
        xaxis_title="Date",
        yaxis_title="Ecart planning ("+str(ts2.iloc[0, 2])+")",
        legend_title="Légende")
    return fig





