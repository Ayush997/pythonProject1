import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
page_3_layout = html.Div(
style={'background-image':'url(/assets/fire2.jpg)',
'background-size': 'cover',
},children=[
    html.H1('Prediction',style={
            'textAlign': 'center',
            'color': '#ffd1b3',
             'font-family': 'Times New Roman',
        }),
    html.H1("Input values for prediction",style={
            'color': '#ffd1b3',
             'font-family': 'Times New Roman',
            'textAlign': 'center',
        }),
    html.Label('Temperature',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='temp',
        placeholder='Insert temperature(F) value',
        type='number',
        value='',
    ),
    html.Br(),
    html.Label('Sunhour',style={'color':'#ffd1b3'}),
    dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='sunhour',
        placeholder='Insert sunhour value',
        type='number',
        value='',
       ),
    html.Br(),
    html.Label('Uv-index',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='uvindex',
        placeholder='Insert uv-index value',
        type='number',value='',

    ),
    html.Br(),
    html.Label('Wind Speed',style={'color':'#ffd1b3'}),
  dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='windspeed',
        placeholder='Insert wind-speed(kmph) value',
        type='number',value='',
    ),
    html.Br(),
    html.Label('Humidity',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='humidity',
        placeholder='Insert humidity value',
        type='number',value='',
    ),
    html.Br(),
    html.Label('Visibility',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='vis',
        placeholder='Insert visibility value',
        type='number',value='',
    ),
    html.Br(),
    html.Label('Pressure',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='pressure',
        placeholder='Insert pressure value',
        type='number',value='',
    ),
    html.Br(),
    html.Label('Heat-index',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='heatindex',
        placeholder='Insert heat index(F) value',
        type='number',value='',

    ),
    html.Br(),
    html.Label('Dew-point',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='dewpoint',
        placeholder='Insert dew point(C) value',
        type='number',value='',

    ),
    html.Br(),
    html.Label('Wind-Gust',style={'color':'#ffd1b3'}),
   dcc.Input(style={'width': '50%',
  'padding': '12px 20px',
  'margin': '8px 0',
  'box-sizing': 'border-box',
   'border': '2px solid green',
  'border-radius': '4px',
  'outline': 'none'},
        id='windgust',
        placeholder='Insert wind gust(kmph) value',
        type='number',value='',

    ),
    html.Br(),
   html.Button('Submit',id='button',type='submit',style={'width': '50%',
  'background-color': '#4CAF50',
  'color': 'white',
  'padding': '14px 20px',
  'margin': '8px 0',
  'border': 'none',
  'border-radius': '4px',
  'cursor': 'pointer'}),

    html.Br(),
    html.Br(),
    html.Div(id='result',style={'color':'#ffd1b3'}),
    html.Br(),
    html.Div(id='page-3-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 4', href='/page-4'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])