import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Ouput

airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})
app =dash.Dash(__name__)

app.layout = html.Div(children=[ html.H1(),
                        html.Div(["Input Year : ", dcc.Input()], html.Br(), html.Br(), html.Div([html.Div(), html.Div()], style = {'display': 'flex'}),
html.Div([
    html.Div(),
    html.Div()
], style = {'display': 'flex'}),

html.DIv(, style = {'width': '65%'})
)])