import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
data = pd.read_csv('pink_morsels.csv')
data['sales'] = data['quantity'] * data['price']
data = data.sort_values(by="date")
data['date'] = pd.to_datetime(data['date'])
app = dash.Dash(__name__)
df = pd.DataFrame(data)
app.layout = html.Div([
    dcc.RadioItems(
        id='region-filter',
        options = [
            {'label': 'All', 'value': 'All'},
            {'label': 'North', 'value': 'North'},
            {'label': 'South', 'value': 'South'},
            {'label': 'East', 'value': 'East'},
            {'label': 'West', 'value': 'West'},
                ],
        value = 'All',
        labelStyle={'display' : 'block'}
    ),
    dcc.Graph(id='sales-line-chart')
])
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-filter', 'value')],
)
def update_graph(selected_region):
    if selected_region == 'All':
        filtered_data = df
    else:
        filtered_data = data[data['region'] == selected_region]
    fig = px.line(filtered_data, x='date', y = 'sales', title='Sales Over Time',
                   labels={'sales': 'Sales ($)', 'date': 'Date'})
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales ($)', xaxis=dict(tickformat='%Y-%m-%d'))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)