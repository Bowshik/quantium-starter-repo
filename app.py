import dash
from dash import dcc, html, Input, Output
import pandas as pd

df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser",
            style={
                'textAlign': 'center',
                'color': '#ff69b4',
                'fontFamily': 'Arial',
                'padding': '20px',
                'backgroundColor': '#1a1a2e'
            }),

    html.Div([
        html.Label("Filter by Region:",
                   style={'color': 'white', 'fontFamily': 'Arial', 'fontSize': '18px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'color': 'white', 'fontFamily': 'Arial', 'fontSize': '16px', 'padding': '10px'}
        )
    ], style={'backgroundColor': '#16213e', 'padding': '20px', 'margin': '10px'}),

    dcc.Graph(id='sales-chart'),

], style={'backgroundColor': '#1a1a2e', 'minHeight': '100vh'})

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df
    else:
        filtered = df[df['region'] == selected_region]

    return {
        'data': [{
            'x': filtered['date'],
            'y': filtered['sales'],
            'type': 'line',
            'name': 'Sales',
            'line': {'color': '#ff69b4'}
        }],
        'layout': {
            'title': 'Pink Morsel Sales Over Time',
            'xaxis': {'title': 'Date', 'color': 'white', 'gridcolor': '#444'},
            'yaxis': {'title': 'Sales ($)', 'color': 'white', 'gridcolor': '#444'},
            'plot_bgcolor': '#16213e',
            'paper_bgcolor': '#1a1a2e',
            'font': {'color': 'white'}
        }
    }

if __name__ == '__main__':
    app.run(debug=True)