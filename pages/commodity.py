import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.io as pio



x = ['Aaron', 'Bob', 'Chris']
y1 = [5, 10, 6]
y2 = [8, 16, 12]

fig = px.bar(x=x, y=[y1,y2],barmode='group')

texts = [y1, y2]
for i, t in enumerate(texts):
    fig.data[i].text = t
    fig.data[i].textposition = 'outside'
  
dash.register_page(__name__,name='Commodity Status')
data = pd.read_excel('assets/data.xlsx', sheet_name='commodity')
layout = html.Div(
    [
        dbc.Row(
            [               
                dbc.Col(
                    [
                            html.P("Commodity Satus",
                           style={"color": "black",
                                  "font-size": "15px",
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'center'
                                  }
                           ),                           
                        ],width=8,
                    className='',
                    xs=6,sm=6,md=6,lg=6,xl=6,xxl=6
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
                    
                            dcc.Graph(figure=fig)
                        
                        ],
                    width=10,
                    className='',
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
                           )    
                        ],
                    className='',
                    xs=6,sm=6,md=6,lg=6,xl=6,xxl=6
                    ),
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
                           )    
                        ],
                    className='',
                    xs=6,sm=6,md=6,lg=6,xl=6,xxl=6
                    ),
                html.Br(),
                ]),      
                        ]),

              








