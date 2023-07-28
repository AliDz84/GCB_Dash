import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd

sheet_id='1Wj2jpW9-r7fzLAmkhBb3ue2nCOhHIcIS'
imageList=pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx", sheet_name='ImgList')
imageList2=pd.read_excel('data.xlsx')
ph1=imageList['Desc'].loc[imageList2.index[0]]
ph1=imageList['Desc'].loc[imageList.index[0]]
ph2=imageList['Desc'].loc[imageList.index[1]]
ph3=imageList['Desc'].loc[imageList.index[2]]
ph4=imageList['Desc'].loc[imageList.index[3]]
ph5=imageList['Desc'].loc[imageList.index[4]]
ph6=imageList['Desc'].loc[imageList.index[5]]

img1=html.Img(src="/assets/logo.jpg",className = 'center')
img2="https://drive.google.com/uc?id=1l4NhluuAtzwFpu9BZYsOL_T1k5h0RCor"
img3="https://drive.google.com/uc?id=1AVLGnDvnkZEgLbv7p8hFtS57CHw2BiK7"
img4="https://drive.google.com/uc?id=1h3w3FwMevLBvVUy0BFXwFzXoKC0tBp6o"
img5="https://drive.google.com/uc?id=1L3cvEgvWb6ytvOHJYZ-QiDBF2sjgsIdb"
img6="https://drive.google.com/uc?id=1t4OCvFe6UNxxSC_psGmRNnrS_tkF6TFh"

dash.register_page(__name__,name='Photos Progress')

layout = html.Div(
    [
  
        dbc.Row(
            [               
                dbc.Col(
                    [
                            html.Img(src="/assets/logo.jpg",style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),

                            html.P(ph1,
                           style={"color": "white",
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
                            html.Img(src=img2,style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph2,
                           style={"color": "white",
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
                            html.Img(src=img3,style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph3,
                           style={"color": "white",
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
                            html.Img(src=img4,style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph4,
                           style={"color": "white",
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
                            html.Img(src=img5,style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph5,
                           style={"color": "white",
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
                            html.Img(src=img6,style={'height':'307px', 'width':'500px','margin-left': '40px'},className = 'center'),
                            html.P(ph6,
                           style={"color": "white",
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

              








