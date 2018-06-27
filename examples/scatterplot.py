import numpy as np
import plotly.graph_objs as go 
import plotly.offline as pyo 

#data
np.random.seed(20)
RANDOM_X = np.random.randint(1, 10, 10)
RANDOM_Y = np.random.randint(1, 10, 10)

#set graph data
data = [go.Scatter(x = RANDOM_X, y = RANDOM_Y, mode = "markers",
                    marker = dict(
                                    size=12,
                                    symbol = 'circle'
                    ))]

#layout
layout = go.Layout(title = 'Example Scatter Plot', 
                   xaxis = {'title': 'RANDOM_X'},
                   yaxis = {'title': 'RANDOM_Y'},
                   hovermode = 'closest')

figure = go.Figure(data = data, layout = layout)

pyo.plot(figure, filename = 'examples/output/scatter.html')
