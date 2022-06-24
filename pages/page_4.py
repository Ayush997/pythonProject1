import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json
candidates = ['Fire Jan 2019','Fire Feb 2019','Fire Mar 2019','Fire Apr 2019','Fire May 2019','Fire Jun 2019','Fire Nov 2019','Fire Dec 2019','Geographical Area','Very dense','Moderately dense','Open forest','Total forest area','% of forested area','Forest cover % change since 2015']

page_4_layout = html.Div([
    html.P("WELCOME TO FIRE DATA VISUALISATION",style={'text-align':'center','font-family':'Times','fontSize':30,'color':'#330000'}),
    html.P("Please make a choice",style={'font-style':'italic','fontSize':19,'font-family':'Times','color':'#880000'}),
    dcc.Dropdown(
        id='candidate',
        options=[{'value': x, 'label': x}
                 for x in candidates],
        value=candidates[0],
        style={'width': '50%', 'display': 'block'}
      #  labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id="choropleth1"),
    html.Div(id='page-4-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
     html.Br(),
    dcc.Link('Go back to home', href='/')
])