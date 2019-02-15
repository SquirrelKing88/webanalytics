import plotly
import plotly.graph_objs as go
import numpy as np
import json
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'development key'

# https://www.kaggle.com/shep312/plotlycountrycodes
# TODO add other countries
world = {
    'Afghanistan': {
        'code': 'AFG',
        'data': {
            'value': 12
        }
    },
    'Albania': {
        'code': 'ALB',
        'data': {
            'value': 100
        }
    },
    'Algeria': {
        'code': 'DZA',
        'data': {
            'value': 300
        }
    },
    'Ukraine': {
        'code': 'UKR',
        'data': {
            'value': 3003
        }
    },
}


# http://127.0.0.1:5000/world?country=Ukraine&value=126

@app.route('/world', methods=['GET'])
def update_world():
    country = request.args.get('country')
    value = request.args.get('value')

    # TODO if value not itn nothing change
    if country in world:
        world[country]['data']['value']= int(value)

    return json.dumps(world)





@app.route('/', methods=['GET'])
def index():
    world_data = pd.DataFrame.from_dict(world)

    data = [dict(
        type='choropleth',

        locations=list(world_data.loc['code',:]),
        # TODO text=...,
        z=[ data['value'] for data in list(world_data.loc['data',:]) ],

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

        autosize=False,
        width=1000,
        height=1000,

        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection=dict(
                type='Mercator'
            )
        )
    )

    fig = {'map': dict(data=data, layout=layout)}

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('graphs.html', graphJSON=graphJSON)



@app.route('/google_graph', methods=['GET'])
def google_graph():

    world_data = [
        ['Country', 'Popularity'],
    ]

    world_data.extend( [ [country, world[country]['data']['value'] ] for country in world] )

    return render_template('google_graphs.html', world_data=world_data)


if __name__ == '__main__':
    app.run(host="localhost", port=8888)
