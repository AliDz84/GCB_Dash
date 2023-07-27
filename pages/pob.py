import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__,name='Personal On Board')
layout = html.Div(
    [
        dbc.Row(
            [               
                dbc.Col(
                    [
                           
                            html.P("1111111",
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
                            
                            html.P("555555555",
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
                            
                            html.P("5555555",
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
                           
                            html.P("8888888",
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
       
                        ]),
              









