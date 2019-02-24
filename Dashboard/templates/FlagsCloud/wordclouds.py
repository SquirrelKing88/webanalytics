import os
import random
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from flask import Flask, render_template, send_file


def flags(frequencies=None,image=None,texts=None):
    text = open(texts).read()
    for word in text.split():
        frequencies.update({word: random.randint(10, 400)})



    flag = np.array(Image.open(image))
    stopwords = set(STOPWORDS)
    stopwords.add("said")
    #TODO cahnge wordclouds parameter values
    wordcloud = WordCloud(background_color="white", max_words=1000, mask=flag,
               stopwords=stopwords, max_font_size=45, random_state=42)

    wordcloud.generate_from_frequencies(frequencies=frequencies)


    image_colors = ImageColorGenerator(flag)
    #TODO add to Flask
    plt.figure(figsize=[7, 7])
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")



    return plt.show()
