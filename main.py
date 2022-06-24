import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
from pages import index
from pages import page_1
from pages import page_2
from pages import page_3
from pages import page_4
from pages.page_1 import external_stylesheets
import json
import pandas as pd
import plotly.express as px
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
import plotly.io as pio

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions = True)
app.title = "Fire Analytics: Understanding Forest Fires!"


data=pd.read_excel(r'D:\college\Minor project\data\telangana.xlsx')
x = data.iloc[:, [1,2,3,4,5,6,7,8,9,10]].values
y= data.iloc[:,[11]].values


dist=json.load(open("DB.json",'r'))
df=pd.read_csv("Forest Covers.csv")
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

dfr = pd.read_csv("2019count.csv")
geojson = json.load(open("indstate2.json",'r'))
candidates = ['Fire Jan 2019','Fire Feb 2019','Fire Mar 2019','Fire Apr 2019','Fire May 2019','Fire Jun 2019','Fire Nov 2019','Fire Dec 2019','Geographical Area','Very dense','Moderately dense','Open forest','Total forest area','% of forested area','Forest cover % change since 2015']
# Page 1 callback
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)

# Page 2
@app.callback(Output("choropleth", "figure"),
           [Input('none', 'children')])

def display_choropleth(self):
    maping_dict = {}
    for feature in dist['features']:
        feature['id'] = feature['properties']['No_HH']
        maping_dict[feature['properties']['Dist_Name']] = feature['id']
    df['id'] = df['Districts1'].apply(lambda x: maping_dict[x])
    fig = px.choropleth(df, locations='id', geojson=dist, color='Forest Cover (Sq. Kms.)', hover_name='Districts',
                        scope='asia')
    # fig.update_geos(fitbounds="locations",visible=False)
    return fig

# Page 3
@app.callback(
    Output('result', 'children'),
    [Input('button','n_clicks')],
     state=[State('temp' ,'value'),
     State('sunhour', 'value'),
     State('uvindex', 'value'),
     State('windspeed', 'value'),
     State('humidity', 'value'),
     State('vis', 'value'),
     State('pressure', 'value'),
     State('heatindex', 'value'),
     State('dewpoint', 'value'),
     State('windgust', 'value')])
def update_result(n_clicks,temp,sunhour,uvindex,windspeed,humidity,vis,pressure,heatindex,dewpoint,windgust):
    CCI = 0.0115791(temp) + 0.066646276(sunhour) + 0.335371568(uvindex)+ 0.192798083(windspeed) + 0.13647433(humidity) + 0.037588404(vis) + 0.0000165598(pressure) + 0.009354098(heatindex) + 0.067435904(dewpoint) + 0.142762765(windgust),
    smote = SMOTE()
    X_smo, Y_smo = smote.fit_resample(x,y.ravel())
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_smo, Y_smo.ravel())
    predicted = clf.predict([[temp,sunhour,uvindex,windspeed,humidity,vis,pressure,heatindex,dewpoint,windgust]])
    return 'The chances of fire happening are {}'.format(predicted)

# Page 4
@app.callback(
    Output("choropleth1", "figure"),
    [Input("candidate", "value")])
def display_choropleth1(candidate):
    mapping_dict = {}
    dfr['State'] = dfr['State'].str.title()
    for feature in geojson['features']:
        feature['id'] = feature['properties']['ID_1']
        mapping_dict[feature['properties']['NAME_1']] = feature['id']
    dfr['id'] = dfr['State'].apply(lambda x: mapping_dict[x])
    text = dfr.apply(lambda row: f"{row['State']}%<br>{row[candidate]}", axis=1)
    fig1 = px.choropleth(dfr,
                        locations='id',
                        geojson=geojson,
                        color=candidate,
                        hover_name='State',
                        scope='asia',
                        color_continuous_scale="PuRd",
                        basemap_visible=True
                        )
    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig1

# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1.page_1_layout
    elif pathname == '/page-2':
        return page_2.page_2_layout
    elif pathname == '/page-3':
        return page_3.page_3_layout
    elif pathname == '/page-4':
        return page_4.page_4_layout
    else:
        return index.index_page



if __name__ == '__main__':
    app.run_server(debug=False)