import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.io as pio









  
dash.register_page(__name__,name='Commodity Status')
data = pd.read_excel('assets/data.xlsx', sheet_name='commodity')
fig = px.histogram(data,x='date', y=['plan','actual'],barmode='group',
              title='custom tick labels with ticklabelmode="period"')
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y",
    )
fig.update_layout(
    autosize=True)
layout = html.Div(
    [
        dbc.Row(
            [               
                dbc.Col(
                    [
dcc.Dropdown(options=[x for x in data.commodity.unique()],id='disc-choice',style={'width':'50%'}),
 
                        ],
                    
                    className='',
                    width=4
                    ),
                                dbc.Col(
                    [

dcc.Dropdown(options=[x for x in data.commodity.unique()],id='disc-choice2',style={'width':'50%'}), 
                        ],
                    
                    className='',
                    width=4
                    ),
                dbc.Col(
                    [
                            html.P("1",
                           style={"color": "black",
                                  "font-size": "15px",
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'center'
                                  }
                           ),
                    
                        
                        
                        ],
                  
                    className='',
                     xs=10,sm=10,md=10,lg=10,xl=10,xxl=10
                    ),
                html.Br(),
                ]),
        dbc.Row(
            [               
                dbc.Col(
                    [
                            html.P("1",
                           style={"color": "black",
                                  "font-size": "15px",
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'center'
                                  }
                           ),
                            dcc.Graph(id='commodity-progress',figure=fig)
                        ],
                    
                    className='',
                    xs=10,sm=10,md=10,lg=10,xl=10,xxl=10
                    ),
                        ])
        ])

@callback(
    Output('commodity-progress', 'figure'),
    Input('disc-choice', 'value'))
def update_output(value):
    ts = data[data.commodity==value]
    fig = px.histogram(ts,x='date', y=['plan','actual'],barmode='group',
              title='custom tick labels with ticklabelmode="periodx123"')
    fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y",
    )
    fig.update_layout(
    autosize=True)
    return fig
              








