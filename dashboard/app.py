from pathlib import Path
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

DATA=Path(__file__).resolve().parents[1]/'data'/'spacex_launch_dash.csv'
df=pd.read_csv(DATA)

app=Dash(__name__)
app.title='SpaceX Falcon 9 Landing Dashboard'

app.layout=html.Div([
    html.H1('SpaceX Falcon 9 Landing Success Dashboard'),
    html.Label('Select launch site'),
    dcc.Dropdown(id='site', options=[{'label':'All sites','value':'ALL'}]+[{'label':x,'value':x} for x in sorted(df['LaunchSite'].dropna().unique())], value='ALL', clearable=False),
    html.Br(),
    dcc.Graph(id='success-pie'),
    html.Label('Payload mass range (kg)'),
    dcc.RangeSlider(id='mass', min=float(df['PayloadMass'].min()), max=float(df['PayloadMass'].max()), value=[float(df['PayloadMass'].min()), float(df['PayloadMass'].max())], step=100, tooltip={'placement':'bottom','always_visible':False}),
    dcc.Graph(id='payload-scatter')
], style={'maxWidth':'1100px','margin':'0 auto','padding':'20px'})

@app.callback(Output('success-pie','figure'), Output('payload-scatter','figure'), Input('site','value'), Input('mass','value'))
def update(site, mass):
    d=df[(df['PayloadMass']>=mass[0])&(df['PayloadMass']<=mass[1])].copy()
    if site!='ALL': d=d[d['LaunchSite']==site]
    pie=d['class'].map({0:'Unsuccessful',1:'Successful'}).value_counts().rename_axis('Outcome').reset_index(name='Count')
    fig1=px.pie(pie,names='Outcome',values='Count',title='Landing outcome share')
    fig2=px.scatter(d,x='FlightNumber',y='PayloadMass',color=d['class'].map({0:'Unsuccessful',1:'Successful'}),hover_data=['LaunchSite','BoosterVersion'],title='Payload mass vs. flight number')
    return fig1,fig2

if __name__=='__main__':
    app.run(debug=True)
