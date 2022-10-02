# import chart_studio.plotly as py
# import plotly.graph_objs as go
# import plotly.figure_factory as ff
#
# import pandas as pd
# from pandas.io import gbq # to communicate with Google BigQuery

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Output, Input
from google.oauth2 import service_account  # pip install google-authimport dash
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Output, Input
from google.oauth2 import service_account


project_id = 'chicagotaxitrips255'
app = dash.Dash(__name__)

myTitle = dcc.Markdown(children='# CHICAGO TAXI TRIPS DATASET DASHBOARD')
myTitle2 = dcc.Markdown(children='# ')
california_graph_title = dcc.Markdown('## Temperature in California')

myGraph2 = dcc.Graph(figure={})



app.layout = dbc.Container(
    [myTitle,myTitle2, california_graph_title,myGraph2, dcc.Store(id='myData', data=[], storage_type="memory")])


@app.callback(
    Output('myData', 'data'),
    Input(myTitle2,'children')
)

def Get_data(val):
    df_chicagotaxifare= pd.read_csv("c:/Users/priyanka/Downloads/dataset.csv")
    print(df_chicagotaxifare)
    return df_chicagotaxifare.to_dict("records")

@app.callback(
    Output(myGraph2, 'figure'),
    Input('myData', 'data')
)

def Update_graph1(df):
    df = pd.DataFrame(df)
    # df = df.sort_values('total_number_of_trips').groupby('payment_type')
    df = df.groupby('payment_type')
    df = df.reset_index()
    print(df)
    df.loc[df['total_number_of_trips'] < 400, 'payment_type'] = 'Others'
    fig = px.pie(df, values='total_number_of_trips', names='payment_type', title='Payment Types in Chicago Taxi')
    return fig


if __name__ == '__main__':
    app.run_server(debug=False)


