import random

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



frequencies = {
            "Ukraine":2000,
            "Poland": 1000,
            "Trump": 200,
        }

text = open('alice.txt').read()
for word in  text.split():
    frequencies.update({word:random.randint(10, 400)})

#

alice_coloring = np.array(Image.open("static/images/ukraine_flag.jpg"))
stopwords = set(STOPWORDS)
stopwords.add("said")

wordcloud = WordCloud(background_color="white", mask=alice_coloring,
               stopwords=stopwords, max_font_size=40)



wordcloud.generate_from_frequencies(frequencies=frequencies)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

plt.figure(figsize=[7,7])
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

# store to file
# plt.savefig("static/images/MonaLisaWords.jpg", format="jpg")

plt.show()
