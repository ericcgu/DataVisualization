import numpy as np
import plotly.graph_objs as go 
import plotly.offline as pyo 

#data
np.random.seed(56)
#generate evenly spaced
X_VALUES = np.linspace(0, 1, 100)
Y_VALUES = np.random.randn(100)
#setup
line1 = go.Scatter(x = X_VALUES,
                   y = Y_VALUES + 5,
                   mode = 'line',
                   name = 'A' )
line2 = go.Scatter(x = X_VALUES,
                   y = Y_VALUES -5,
                   mode = 'line',
                   name = 'B' ) 
line3 = go.Scatter(x = X_VALUES,
                   y = Y_VALUES,
                   mode = 'lines+markers',
                   name = 'C' )                                         

data = [line1, line2, line3]
#layout
layout = go.Layout(title = 'Example Line Chart', 
                   xaxis = {'title': 'RANDOM_X'},
                   yaxis = {'title': 'RANDOM_Y'},
                   hovermode = 'closest')

figure = go.Figure(data = data, layout = layout)

pyo.plot(figure, 
        filename = 'examples/linechart/linechart.html', 
        config={"displayModeBar": False}, 
        show_link = False)
    