from flask import Flask,jsonify
from database import *

app=Flask(__name__)

@app.route("/data")
def checkConnection():
    return jsonify(laptop.objects.all())

@app.route("/data1")
def srivignesh():
    return jsonify(laptop.objects.all())


app.config['MONGODB_HOST']=url
mydata.init_app(app)

if __name__=="__main__":
    app.run(debug=True,port=2328)