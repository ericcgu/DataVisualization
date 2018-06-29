
import plotly.offline as pyo
import plotly.graph_objs as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]
y2 = [16, 12,27]

trace1 = go.Bar(
    x=y,
    y=x,
    text=y,
    textposition = 'auto',
    orientation = 'h',
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.6
)

trace2 = go.Bar(
    x=y2,
    y=x,
    text=y2,
    orientation = 'h',
    textposition = 'auto',
    marker=dict(
        color='rgb(58,200,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5),
        ),
    opacity=0.6
)

data = [trace1,trace2]

pyo.plot(data, filename='examples/barchart/barchart.html')