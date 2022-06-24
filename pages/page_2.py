import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import pandas as pd
import plotly.express as px
import plotly.io as pio

page_2_layout = html.Div([
    html.H1('Telangana Forest Cover'),
     html.Div(id='none',children=[],style={'display': 'none'}),
    dcc.Graph(id="choropleth"),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to Page 4', href='/page-4'),
     html.Br(),
    dcc.Link('Go back to home', href='/')
])