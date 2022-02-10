import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque
import requests


def tempDados():
    proxies = {'https':"https://disrct:saladigital0311@10.224.200.26:8080"}
    url_temperatura = 'https://prova-dht-default-rtdb.firebaseio.com/Sensor/temperatura.json'
    temperatura_data = float(requests.get(url_temperatura, proxies=proxies).content)
    return temperatura_data

def umiDados():
    proxies = {'https':"https://disrct:saladigital0311@10.224.200.26:8080"}
    url_umidade = 'https://prova-dht-default-rtdb.firebaseio.com/Sensor/umidade.json'
    umidade_data = float(requests.get(url_umidade, proxies=proxies).content)
    return umidade_data

X = deque(maxlen = 20)
X.append(0)
  
Y = deque(maxlen = 200)
Y.append(0)
  
app = dash.Dash(__name__)
  
app.layout = html.Div(
    [
        html.H1(children='Gráfico Umidade '),

        html.Div(children='''
            Dash: Umidade em tempo real:
        '''),
        
        dcc.Graph(id = 'live-graph', animate = True),
        dcc.Interval(
            id = 'graph-update',
            interval = 5000,
            n_intervals = 1
        ),
    ]
)
  
@app.callback(
    Output('live-graph', 'figure'),
    [ Input('graph-update', 'n_intervals') ]
)
  
def update_graph_scatter(n):
    valor = float(umiDados())
    X.append(X[-1]+1)
    Y.append(valor)
  
    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
    )
  
    return {'data': [data],
            'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]),)}
  
if __name__ == '__main__':
    app.run_server(debug=False)