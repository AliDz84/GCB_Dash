import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import glob

img=glob.glob("assets/*.jpg")
ph1=img[0][7:-4]
ph2=img[1][7:-4]
ph3=img[2][7:-4]
ph4=img[3][7:-4]
ph5=img[4][7:-4]
ph6=img[5][7:-4]
dash.register_page(__name__,name='Photos Progress')
layout = html.Div(
    [
        dbc.Row(
            [               
                dbc.Col(
                    [
                            html.Img(src=img[0],style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),

                            html.P(ph1,
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
                            html.Img(src=img[1],style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph2,
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
                            html.Img(src=img[2],style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph3,
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
                            html.Img(src=img[3],style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph4,
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
                            html.Img(src=img[4],style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph5,
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
                            html.Img(src=img[5],style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph6,
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

              








