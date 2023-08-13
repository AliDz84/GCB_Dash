import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go


dash.register_page(__name__,name='Commodity Status')
#read data from database
data = pd.read_excel('assets/data.xlsx', sheet_name='commodity')

fig = px.histogram(data,x='date', y=['Planifié','Réalisé'],barmode='group',
              title="Avancements mensuels de: "+"Béton armé (m3)")
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
        dcc.Dropdown(options=['Avancements mensuels', 'Avancements cumulés', 'Ecarts planning'],id='menu',value="Avancements mensuels",style={'width':'90%'}),
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
                html.Div(id='qty-totale',children="non",style={
                        'backgroundColor':'DarkOrange',
                        'color':'white',
                        'font-weight': 'bold',
                        "border-style": "ridge",
                        'height':'40px',
                        'text-align':'center',
                        'width':'80%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
             dbc.Col(
                    [
                html.Div(id='cum-act-qty',children="non", style={
                        'backgroundColor':'blue',
                        'color':'white',
                        'font-weight': 'bold',
                        "border-style": "ridge",
                        'height':'40px',
                        'text-align':'center',
                        'width':'80%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
                         dbc.Col(
                    [
                html.Div(id='cum-act-qty-percent',children="non", style={
                        'backgroundColor':'BlueViolet',
                        'color':'white',
                        'font-weight': 'bold',
                        "border-style": "ridge",
                        'height':'40px',
                        'text-align':'center',
                        'width':'80%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
                                      dbc.Col(
                    [
                html.Div(id='cum-planning-qty',children="non", style={
                        'backgroundColor':'Green',
                        'color':'white',
                        'font-weight': 'bold',
                        "border-style": "ridge",
                        'height':'40px',
                        'text-align':'center',
                        'width':'80%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
                dbc.Col(
                    [
                html.Div(id='ecart-planning',children="non", style={
                        'backgroundColor':'Magenta',
                        'color':'white',
                        'font-weight': 'bold',
                        "border-style": "ridge",
                        'height':'40px',
                        'text-align':'center',
                        'width':'80%',
                        'display':'inline-block'
               })  
                        ],
                    className='h-50',

                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
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
    if value1=="Avancements mensuels":
        ts = data[data.commodity==value2]
        fig = px.histogram(ts,x='date', y=['Planifié','Réalisé'],barmode='group',
        title="Avancement mensuel de: "+value2)
        fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",)
        fig.update_layout(
        autosize=True,
        xaxis_title="Date",
        yaxis_title="Quantité",
        legend_title="Légende")
    if value1=="Avancements cumulés":
        ts = data[data.commodity==value2]
        trace_1 = go.Scatter(x=ts['date'], y=ts['Cum plan'], mode='lines', line=dict(color="orange"),name='Qty prévue')
        trace_2 = go.Scatter(x=ts['date'], y=ts['Cum actual'], mode='lines', line=dict(color="blue"),name='Qty réalisée',)
        fig = go.Figure([
        trace_1, trace_2
        ])
        fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",)
        fig.update_layout(
        autosize=True,
        xaxis_title="Date",
        yaxis_title="Avancements cumulés %",
        legend_title="Légende",
        title="Avancements cumulés de "+str(value2))
       
    if value1=="Ecarts planning":
        ts = data[data.commodity==value2]
        fig = px.bar(ts,x='date', y=['Ecart'],
        title="Ecart planning de "+str(value2))
        fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",)
        fig.update_layout(
        autosize=True,
        xaxis_title="Date",
        yaxis_title="Avancements cumulés %",
        legend_title="Légende")

    return fig

@callback(
    Output('qty-totale', 'children'),
    Input('commodity-choice', 'value'))    
def update_output(value):
    ts = data[data.commodity==value]
    children="Qty Totale: "+"{:.0f}".format(ts['Scope'].sum())+" "+str(ts.iloc[0, 2])
    return children
@callback(
    Output('cum-act-qty', 'children'),
    Input('commodity-choice', 'value'))
def update_output(value):
    ts = data[data.commodity==value]
    children="Cum qty Réalisée: "+"{:.0f}".format(ts['Cum actual'].sum())+" "+str(ts.iloc[0, 2])
    return children
@callback(
    Output('cum-act-qty-percent', 'children'),
    Input('commodity-choice', 'value'))
def update_output(value):
    ts = data[data.commodity==value]
    children="% Qty Réalisée: "+"{:.1%}".format(ts['Cum actual'].sum()/ts['Scope'].sum())
    return children
@callback(
    Output('cum-planning-qty', 'children'),
    Input('commodity-choice', 'value'))
def update_output(value):
    ts = data[data.commodity==value]
    ts = data[data.commodity==value]
    ts = ts.loc[ts['Réalisé'].notnull()]
    children="Qty Planifiée: "+"{:.0f}".format(ts['Cum plan'].sum())+" "+str(ts.iloc[0, 2])
    return children
@callback(
    Output('ecart-planning', 'children'),
    Input('commodity-choice', 'value'))
def update_output(value):
    ts = data[data.commodity==value]
    ts = ts.loc[ts['Réalisé'].notnull()]
    children="Ecart planning: "+"{:.0f}".format(ts['Cum var'].sum())+" "+str(ts.iloc[0, 2])
    return children



