import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


app=dash.Dash(__name__,use_pages=True,external_stylesheets=[dbc.themes.SPACELAB])
server = app.server
sidebar=dbc.Nav(
    [
        dbc.NavLink(
            [
            html.Div(page["name"],className="lead"),
            ],
            href=page["path"],
            active="exact",
            )
        for page in dash.page_registry.values()
        ],
    vertical=True,
    pills=True,
    className="bg-Blue",
            )
app.layout=dbc.Container([

        dbc.Row(
        [
        dbc.Col([
            html.Img(src="assets/logo.png",className = 'left',style={'margin-top': '20px','margin-left':'20px'}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
                   
            sidebar
            ],xs=2,sm=2,md=2,lg=2,xl=2,xxl=2),
        dbc.Col(
                [
            dbc.Row(
                [           
            html.Div("CONSTRUCTION OF SEPARATION AND DECARBONATION UNITS AT ALRAR EPC2 LOT 1",
                        style={'frontsize':'50','textAlign':'left','color':'#ffffff','margin-top':'20px','background-color':'#EC5832'}),
            html.Div("- DASHBOARD",
                        style={'frontsize':'50','bold':'True','textAlign':'left','color':'#ffffff','background-color':'#EC5832'}),
            html.Hr(),
                    ]),
            dbc.Row(
                [
                    dash.page_container
                    ],)
            ])
            ]
        ),

    ],fluid=True)

   

if __name__ == '__main__':
    app.run()
