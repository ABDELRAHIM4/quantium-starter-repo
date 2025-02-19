import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
from plotly.express import bar, scatter, scatter_matrix, box, violin, histogram, density_contour, line, area
import output, sys
 

data = pd.read_csv('pink_morsels.csv')

data['sales'] = data['quantity'] * data['price']
data = data.sort_values(by="date")
data['date'] = pd.to_datetime(data['date'])
app = Dash(__name__)
# Create a bar chart using Plotly Express
fig = px.line(data,  x='sales', y='date',
             title='Sales of Pink Morsels by Date and Region')

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Visualizer'),

    html.Div(children='''
        This application visualizes the sales data for Pink Morsels.
    '''),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)