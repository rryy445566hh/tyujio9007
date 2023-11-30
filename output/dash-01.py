import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input1', type='number', placeholder='�����һ������'),
    dcc.Input(id='input2', type='number', placeholder='����ڶ�������'),
    html.Button('���', id='submit-button', n_clicks=0),
    html.Div(id='result')
])

@app.callback(
    Output('result', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('input1', 'value'),
     dash.dependencies.State('input2', 'value')]
)
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        return f'��ͽ����{float(input1) + float(input2)}'
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
