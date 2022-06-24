import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
data = pd.read_excel('telangana.xlsx')
#print(data.head())
data["weather_date"] = pd.to_datetime(data["weather__date"], format="%Y-%m-%d")
data.sort_values("weather__date", inplace=True)
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
page_1_layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🔥", className="header-emoji"),
                html.H1(
                    children="Fire Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the behavior of Forest Fires",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="Fire-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["Fire 1"],
                                    "type": "bar",

                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Fires in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {

                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="temp-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["weather__mintempF"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Temperatures in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",


                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
html.Div( children=dcc.Graph(
                        id="Sun-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["weather__sunHour"],
                                    "type": "lines",

                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Sun-hour in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {

                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="Uv-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["weather__uvIndex"],
                                    "type": "Bar",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Uv Index in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",


                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="Wind-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["weather__hourly__windspeedKmph"],
                                    "type": "Bar",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Wind Speed in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",

                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),

                html.Div(
                    children=dcc.Graph(
                        id="Humidity-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["weather__hourly__humidity"],
                                    "type": "Bar",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Humidity in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",

                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
html.Div(
                    children=dcc.Graph(
                        id="Heat Index",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["weather__date"],
                                    "y": data["weather__hourly__HeatIndexF"],
                                    "type": "bar",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Heat Index in Bhupalpally",
                                    "x": 0.05,
                                    "xanchor": "left",

                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#ff6600"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),

html.Div(id='page-1-content'),
html.Br(),
dcc.Link('Go to Page 2', href='/page-2'),
html.Br(),
dcc.Link('Go to Page 3', href='/page-3'),
html.Br(),
dcc.Link('Go to Page 4', href='/page-4'),
html.Br(),
dcc.Link('Go back to home', href='/'),

])