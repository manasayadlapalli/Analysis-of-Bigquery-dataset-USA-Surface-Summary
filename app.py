import pandas as pd
import plotly.express as px
import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
print(np.pi)

app = Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            html.H1(children='Public dataset "Global Surface Summary of the Day Weather Data" - Hot states in USA (2022)'),
            html.H2('Line chart respresentation'),
             html.Button("Switch Axis", n_clicks=0, 
                id='button'),
                 dcc.Graph(id="graph"),

        ],  className="six columns"),
     ]),
    

    html.Div([
            html.H2('Histogram respresentation'),
               dcc.Graph(id="bar"),
               ], className="six columns"),
    
    html.Div([
        html.Div([
        html.H1(['USA State map']),
      ]),

    html.Div([
        dcc.Graph(id='map')
    ]),
    ])
], className="row")


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv(r'data.csv') 
    if n_clicks % 2 == 0:
        x, y = 'celsius', 'state'
    else:
        x, y = 'state', 'celsius'
    fig = px.line(df, x=x, y=y)    
    return fig

@app.callback(
    Output("bar", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv(r'data.csv')
    if n_clicks % 2 == 0:
        y, x = 'celsius', 'state'
    else:
        y, x = 'state', 'celsius'
    fig1 = px.bar(df, x=x, y=y)    
    return fig1

@app.callback(
     Output("map", "figure"), 
    Input("button", "n_clicks"))

def update_graph(my_dropdown):
     data = pd.read_csv(r'data.csv')  
     fig2 = px.choropleth(data, locations='state',
                     locationmode="USA-states", color='celsius', scope="usa") 
     #fig2.show()    
     return fig2

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)




