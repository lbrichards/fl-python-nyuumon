import numpy as np
import plotly.graph_objs as go

x = np.linspace(-3, 3, 200)
y = np.exp(x**2)**-0.5

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='black'), name="f(x)"))

highlighted_region_1 = np.where((x > -3) & (x < -1), y, None)
highlighted_region_2 = np.where((x > 1) & (x < 3), y, None)

fig.add_trace(go.Scatter(x=x, y=highlighted_region_1, fill='tozeroy', fillcolor='rgba(0, 128, 0, 0.3)', line=dict(color='rgba(0, 0, 0, 0)'), showlegend=False))
fig.add_trace(go.Scatter(x=x, y=highlighted_region_2, fill='tozeroy', fillcolor='rgba(0, 128, 0, 0.3)', line=dict(color='rgba(0, 0, 0, 0)'), showlegend=False))

fig.update_layout(title="f(x)", showlegend=True, xaxis=dict(showgrid=True), yaxis=dict(showgrid=True))

fig.show()
