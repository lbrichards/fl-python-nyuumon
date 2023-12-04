import plotly.graph_objs as go

x = [0, 1]
y = [1, 0]

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

fig.show()
