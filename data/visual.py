import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import output, sys
 
app = Dash()
data = pd.read_csv('pink_morsels.csv')
data['sales'] = data['quantity'] * data['price']
data['date'] = pd.to_datetime(data['date'])
fig = px.bar(data, y="date", x="sales", color="region", barmode="group")
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)