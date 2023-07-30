import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import glob


dash.register_page(__name__,name='Commodity Status')
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
                           )   
                        ],
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
                           )    
                        ],
                    className='',
                    xs=6,sm=6,md=6,lg=6,xl=6,xxl=6
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

              







