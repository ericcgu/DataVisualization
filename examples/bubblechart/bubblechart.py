import plotly.offline as pyo
import plotly.graph_objs as go

data = [
    {
        'x': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
        'y': [1, 3.2, 5.4, 7.6, 9.8, 12.5],
        'mode': 'markers',
        'marker': {
            'color': [120, 125, 130, 135, 140, 145],
            'size': [20, 30, 50, 72, 84, 85],
            'showscale': True
        }
    }
]

pyo.plot(data, filename='examples/bubblechart/bubblechart.html')