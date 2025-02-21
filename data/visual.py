import pandas as pd
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
from plotly.express import bar, scatter, scatter_matrix, box, violin, histogram, density_contour, line, area
import output, sys

data = pd.read_csv('pink_morsels.csv')
data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Ensure 'date' is datetime and handle errors
data = data.dropna(subset=['date'])  # Drop rows with invalid dates
data['sales'] = data['quantity'] * data['price']
data = data.sort_values(by="date")

app = Dash(__name__)
# Create a line chart using Plotly Express
fig = px.line(data, x='date', y='sales', title='Pink Morsels Sales Before and After Price Increase (Feb 15, 2018)',
              labels={'date': 'Date', 'sales': 'Sales ($)'})


fig.add_shape(type="line",
              x0='2018-02-15', x1='2018-02-15',
              y0=0, y1=1,
              line=dict(color="red", width=2, dash="dash"),
              xref="x", yref="paper")

fig.add_annotation(x='2018-02-15', y=1,
                  text="Price Increase",
                  showarrow=False,
                  yshift=10,
                  xanchor="left")



# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Analysis: Impact of Price Increase'),

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
