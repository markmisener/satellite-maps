from flask import Flask, request, render_template
import json


# configure flask app
app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE', silent=True)

# get access token from config file
MAPBOX_ACCESS_TOKEN = app.config['MAPBOX_ACCESS_TOKEN']

# display at homepage path
@app.route('/')
def display():
    return render_template('index.html', MAPBOX_ACCESS_TOKEN=MAPBOX_ACCESS_TOKEN)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
