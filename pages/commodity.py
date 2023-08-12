import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd



dash.register_page(__name__,name='Commodity Status')
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
Scope=10
layout = html.Div(
    [
        dbc.Row(
            [               
             dbc.Col(
                    [
dcc.Dropdown(options=[x for x in data.commodity.unique()],id='commodity-choice',value="Béton armé",style={'width':'80%'}),
                        ],
                    className='',
                    xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
             dbc.Col(
                    [
                html.Div(id='qty-totale',children="non", style={
                        'backgroundColor':'Orange',
                        'color':'white',
                        'font-weight': 'bold',
                        'height':'30px',
                        'margin-left':'0px',
                        'text-align':'center',
                        'width':'70%',
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
                        'height':'30px',
                        'margin-left':'0px',
                        'text-align':'center',
                        'width':'70%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
                         dbc.Col(
                    [
                html.Div(id='cum-act-qty-percent',children="non", style={
                        'backgroundColor':'Black',
                        'color':'white',
                        'font-weight': 'bold',
                        'height':'30px',
                        'margin-left':'0px',
                        'text-align':'center',
                        'width':'70%',
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
                        'height':'30px',
                        'margin-left':'0px',
                        'text-align':'center',
                        'width':'70%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
                   xs=2,sm=2,md=2,lg=2,xl=2,xxl=2
                    ),
                dbc.Col(
                    [
                html.Div(id='ecart-planning',children="non", style={
                        'backgroundColor':'Tomato',
                        'color':'white',
                        'font-weight': 'bold',
                        'height':'30px',
                        'margin-left':'0px',
                        'text-align':'center',
                        'width':'70%',
                        'display':'inline-block'
               })  
                        ],
                    className='',
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
                            dcc.Graph(id='commodity-progress',figure=fig)
                        ],
                    className='',
                    xs=12,sm=12,md=12,lg=12,xl=12,xxl=12
                    ),
                        ])
        ])
@callback(
    Output('commodity-progress','figure'),
    Input('commodity-choice', 'value')
)
    
def update_output(value):
    ts = data[data.commodity==value]
    fig = px.histogram(ts,x='date', y=['Planifié','Réalisé'],barmode='group',
    title="Avancement mensuel de: "+value)
    fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y",)
    fig.update_layout(
    autosize=True,
    xaxis_title="Date",
    yaxis_title="Quantité",
    legend_title="Légende")
    return fig

@callback(
    Output('qty-totale', 'children'),
    Input('commodity-choice', 'value')
)
    
def update_output(value):
    ts = data[data.commodity==value]
    children="Qty Totale: "+"{:.0f}".format(ts['Scope'].sum())+" "+str(ts.iloc[0, 2])
    return children


@callback(
    Output('cum-act-qty', 'children'),
    Input('commodity-choice', 'value')
)
    
def update_output(value):
    ts = data[data.commodity==value]
    children="Cum qty Réalisée: "+"{:.0f}".format(ts['Cum actual'].sum())+" "+str(ts.iloc[0, 2])
    return children

@callback(
    Output('cum-act-qty-percent', 'children'),
    Input('commodity-choice', 'value')
)
def update_output(value):
    ts = data[data.commodity==value]
    children="% Qty Réalisée: "+"{:.1%}".format(ts['Cum actual'].sum()/ts['Scope'].sum())
    return children

@callback(
    Output('cum-planning-qty', 'children'),
    Input('commodity-choice', 'value')
)
def update_output(value):
    ts = data[data.commodity==value]
    ts = data[data.commodity==value]
    ts = ts.loc[ts['Réalisé'].notnull()]
    children="Qty Planifiée: "+"{:.0f}".format(ts['Cum plan'].sum())+" "+str(ts.iloc[0, 2])
    return children

@callback(
    Output('ecart-planning', 'children'),
    Input('commodity-choice', 'value')
)
def update_output(value):
    ts = data[data.commodity==value]
    ts = ts.loc[ts['Réalisé'].notnull()]
    children="Ecart planning: "+"{:.0f}".format(ts['Cum var'].sum())+" "+str(ts.iloc[0, 2])
    return children

