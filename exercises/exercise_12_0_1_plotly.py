import plotly.graph_objs as go

x = [0, 1]
y = [1, 0]

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', line=dict(color='rgba(0, 128, 0, 0.4)', width=10), name="straight line"))

fig.update_layout(title="My first plot", showlegend=True, xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))

fig.show()
