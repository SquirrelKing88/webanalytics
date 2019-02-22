
import json
from os import listdir
from os.path import isfile, join

import os
import random

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from PIL import Image
import numpy as np

from flask import Flask, render_template



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
                                "value": 10,
                                "color": '#e4'
                            },
                            {
                                "category": "boba",
                                "value": 30,
                                "color": '#e4'
                            },
                            {
                                "category": "boban",
                                "value": 100,
                                "color": '#e4'
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
                    "value": 200,
                    "color": '#e4'
                },
                {
                    "category": "Category #2",
                    "value": 300,
                    "color": '#e4'
                }
            ]
        },

    ]

    data_json = json.dumps(pie_data)


    return render_template('index.html', data_json=data_json)



@app.route('/update_clouds', methods=['GET'])
def update_clouds():
    frequencies = {
        "Ukraine": 2000,
        "Poland": 1000,
        "Trump": 200,
    }
    text = open('alice.txt').read()
    for word in text.split():
        frequencies.update({word: random.randint(10, 400)})


    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, 'static', 'images','flags')
    path_save = os.path.join(dir_path, 'static', 'images','clouds')
    files = [file for file in listdir(path) if isfile(join(path, file))]

    for file in files:
        # TODO in THREAD!!!!

        flag = np.array(Image.open(os.path.join(path,file)))

        # TODO check if we need stop words
        stopwords = set(STOPWORDS)
        stopwords.add("said")



        # TODO change wordclouds parameter values
        wordcloud = WordCloud(background_color="white", max_words=1000, mask=flag,
                              stopwords=stopwords, max_font_size=50, random_state=42)

        wordcloud.generate_from_frequencies(frequencies=frequencies)
        image_colors = ImageColorGenerator(flag)
        wordcloud.recolor(color_func=image_colors)

        wordcloud.to_file(os.path.join(path_save,file))
        print('Done for ',file)

    return 'Done'


@app.route('/clouds', methods=['GET'])
def clouds():


    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, 'static', 'images','clouds')
    files = [file for file in listdir(path) if isfile(join(path, file))]


    dataset = dict()

    for file in files:
        country = file

        dataset.update(
                        {
                            country:{
                                        'image':file
                                    }
                        }
                     )
    return render_template('flagclouds.html', dataset=dataset)



if __name__ == '__main__':
    app.run(host="localhost", port=8888)