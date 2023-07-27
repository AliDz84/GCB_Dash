from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                            html.P('Ali LAAKEL '
                           'programming, overcoming complex challenges, proficient in predictive data'
                           ' modeling, processing, visualizing, dashboards, and extracting actionable insights from '
                           'data.',
                           style={"color": "black",
                                  "font-size": "15px",
                                  'margin-left': '100px',
                                  'margin-right': '15px',
                                  'margin-top': '15px',
                                  'margin-bottom': '15px',
                                  'line-height': '1.2',
                                  'text-align': 'justify'
                                  }
                           ),
                        ],
                    className='bg-white'
                    ),
                dbc.Col(
                    [
                        html.P('Distribution of Continuous Variable')
                    ],
                    className='bg-dark text-white'
                    )
            ],
            style={"height": "50vh"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Correlation Matrix Heatmap')
                    ],
                    className='bg-light'
                    )
            ],
            style={"height": "50vh"}
            )
        ]
    )
