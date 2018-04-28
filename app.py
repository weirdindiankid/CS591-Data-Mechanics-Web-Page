from flask import Flask
from flask import render_template
from flask import send_file
import json
import geopandas as gpd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/satisfactionPoints/<month>")
def satisfactionPoints(month):
    satisfactionPoints = gpd.read_file("./data/satisfactionPoints.geojson")
    pointsOfIntrest = satisfactionPoints[["m"+str(month), 'geometry']]
    return json.dumps(pointsOfIntrest.to_json())

@app.route("/map")
def getMap():
    with open("./data/boston.geojson") as f:
        return json.dumps(f.read())


@app.route('/get_image')
def get_image():
    return send_file("./data/rat.png", mimetype='image/png')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)