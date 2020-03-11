from flask import Flask, request, jsonify, Response
import csv
import json
import sqlite3
import datetime
import random
import circle_eval as ce

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port="8000")
