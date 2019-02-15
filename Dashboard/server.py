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
    'Ukraine': {
        'code': 'UKR',
        'coordinates':{
                        'latitude':50.45466,
                        'longitude':30.5238
                      },
        'information': {
                        # all in English
                        'persons':{'bob','boba'},

                        'organizations':{'org1', 'org2'},

                        'locations':{'location 1','location2'}
                        },
                },

    'Poland':{
        'code': None,
        'coordinates':{
                        'latitude':52.237049,
                        'longitude': 21.017532
                      },
        'information': {
                        # all in English
                        'persons':{'bob pl','boba pl'},

                        'organizations':{'org2', 'org2'},

                        'locations':{'location 4','location5'}

                       },
    }
}



@app.route('/', methods=['GET'])
def index():

    # TODO somehow create this dataset


    pie_data = [
        {
            "title": "Ukraine",
            "latitude": 50.45466,
            "longitude": 30.5238,
            "width": 50,
            "height": 50,
            "pieData": [
                            {
                                "category": "bob",
                                "value": 10
                            },
                            {
                                "category": "boba",
                                "value": 30
                            },
                            {
                                "category": "boban",
                                "value": 100
                            }
                        ]
        },

        {
            "title": "Poland",
            "latitude": 52.237049,
            "longitude": 21.017532,
            "width": 50,
            "height": 50,
            "pieData": [
                {
                    "category": "Category #1",
                    "value": 200
                },
                {
                    "category": "Category #2",
                    "value": 300
                }
            ]
        },

    ]

    data_json = json.dumps(pie_data)


    return render_template('index.html', data_json=data_json)







if __name__ == '__main__':
    app.run(host="localhost", port=8888)
