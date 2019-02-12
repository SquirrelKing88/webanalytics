import plotly
import plotly.graph_objs as go
import numpy as np
import json

from flask import Flask, render_template



app = Flask(__name__)
app.secret_key = 'development key'





@app.route('/', methods=['GET'])
def index():
    x = np.linspace(-np.pi, np.pi, 50)
    y = np.sin(x)

    line = go.Scatter(
        x=x,
        y=y,
        name="sin(x)"
    )

    bar = go.Bar(
        x=["House", "Car"],
        y=[100, 300]
    )




    data = {
            'line_id':{
                        'data':[line],
                        'layout':dict(title='first graph')
                     },

            'bar_id':  {
                        'data':[bar],
                        'layout': dict(title='second graph')
                    }

            }
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)



    return render_template('graphs.html', graphJSON=graphJSON)





if __name__ == '__main__':
    app.run()