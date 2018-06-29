import plotly.offline as pyo
import plotly.graph_objs as go

trace0 = go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[50, 17, 14, 10, 5][::-1],
    marker=dict(
        color=['rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(204,204,204,1)', 'rgba(204,204,204,1)',
               'rgba(222,45,38,0.8)']),
)

data = [trace0]
layout = go.Layout(
    title='Least Used Feature',
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(data, filename='examples/barchart/barchart2.html')