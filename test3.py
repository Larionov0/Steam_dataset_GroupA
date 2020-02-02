import plotly

figure = plotly.subplots.make_subplots(rows=2, cols=2)
diag = plotly.graph_objs.Bar(x=["a", "b", "c"], y=[1, 2, 5])
figure.append_trace(diag, 1, 1)

plotly.offline.plot(figure)
