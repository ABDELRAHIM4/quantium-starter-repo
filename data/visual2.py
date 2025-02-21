import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px

data = pd.read_csv('pink_morsels.csv')
data['sales'] = data['quantity'] * data['price']
data = data.sort_values(by="date")
data['date'] = pd.to_datetime(data['date'])

app = Dash(__name__)
# Create a bar chart using Plotly Express
fig = px.bar(data, x='date', y='sales', title='Pink Morsels Sales Before and After Price Increase (Feb 15, 2018)',
             labels={'date': 'Date', 'sales': 'Sales ($)'},
             text=[f'{x:.0f}' if x == int(x) else f'{x:.2f}'.rstrip('0').rstrip('.') for x in data['sales']])

fig.add_vline(x=pd.to_datetime('2018-02-15'), line_width=2, line_dash="dash", line_color="red",
              annotation_text="Price Increase", annotation_position="top left")

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Analysis: Impact of Price Increase'),

    html.Div(children='''
        This application visualizes the sales data for Pink Morsels using a bar chart.
    '''),

    dcc.Graph(
        id='sales-bar-graph',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
