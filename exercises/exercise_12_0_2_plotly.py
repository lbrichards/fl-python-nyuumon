import numpy as np
import plotly.graph_objs as go

x = np.linspace(-3, 3, 200)
y = 4 * x ** 3 + x ** 2

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines', line=dict(color='black'), name="f(x)"))

fig.update_layout(title="f(x)", showlegend=True, xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))

fig.show()
