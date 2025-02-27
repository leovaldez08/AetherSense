import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import random
from datetime import datetime

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0)  
])

@app.callback(
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    new_data = {
        'Timestamp': [datetime.now()],
        'Temperature': [random.uniform(20, 30)],
        'Humidity': [random.uniform(40, 60)],
        'Air Quality (PPM)': [random.uniform(100, 300)],
        'AQI': [random.uniform(50, 150)]
    }
    df = pd.DataFrame(new_data)

    fig = px.line(df, x='Timestamp', y=['Temperature', 'Humidity', 'Air Quality (PPM)', 'AQI'],
                  title='Real-Time Air Quality Monitoring')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)