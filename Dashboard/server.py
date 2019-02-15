import plotly
import plotly.graph_objs as go
import numpy as np
import json
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'development key'


world={
            'Ukraine': 10,
            'Poland': 12
        }

# http://127.0.0.1:5000/world?country=Ukraine&value=126

@app.route('/world', methods=['GET'])
def update_world():
   country = request.args.get('country')
   value = request.args.get('value')

   if country in world:
       world[country] = value

   return json.dumps(world)



@app.route('/', methods=['GET'])
def index():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

    data = [dict(
        type='choropleth',
        locations=df['CODE'],
        z=df['GDP (BILLIONS)'],
        text=df['COUNTRY'],
        colorscale=[[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], \
                    [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
        autocolorscale=False,
        reversescale=True,
        marker=dict(
            line=dict(
                color='rgb(180,180,180)',
                width=0.5
            )),
        colorbar=dict(
            autotick=False,
            title='test'),
    )]

    layout = dict(

        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection=dict(
                type='Mercator'
            )
        )
    )

    fig = dict(data=data, layout=layout)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('graphs.html', graphJSON=graphJSON)



if __name__ == '__main__':
    app.run()