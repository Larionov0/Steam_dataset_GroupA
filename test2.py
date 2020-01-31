import plotly
import plotly.graph_objects as go

x = ['Динозавры', "Пуперы", "Хейтеры", "Лолеры"]
y = [14, 12, 15, 3]


diagram1 = go.Bar(x=x, y=y, name='Marks')
diagram2 = go.Pie(labels=x, values=y, name="Marks")
figure = [diagram1]
plotly.offline.plot(figure, filename='marks.html')
