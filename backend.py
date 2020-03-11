from flask import Flask, request, jsonify, Response
import csv
import json
import sqlite3
import cv2
import datetime
import random
import circle_eval as ce

app = Flask(__name__)


@app.route("/api/uploadImage", methods=['POST'])
def uploadImage():
    data = request.files


    f = open("image.jpg", "w")
    f.truncate()
    f.close()
    with open('image.jpg', 'wb') as f:
        f.write(data["myFile"].read())

    
    return "done"




if __name__ == '__main__':

    a = ce.parseArguments([])
    ce.main(a)
    app.run(host= '0.0.0.0', port="8000")
