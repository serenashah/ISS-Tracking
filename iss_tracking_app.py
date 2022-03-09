from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def get_data():
    return 0

@app.route('/how_to_use', methods=['GET'])
def how_to_use():
    return 0

@app.route('/epochs', methods=['GET'])
def epoch_info():
    return 0

@app.route('/countries', methods=['GET'])
def all_countries():
    return 0

@app.route('/countries/<country>', methods=['GET'])
def specific_country(country):
    return 0

@app.route('/countries/<country>/regions', methods=['GET'])
def all_regions(country):
    return 0

@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def specific_region(country, region):
    return 0

@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def all_cities(country, region):
    return 0

@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GE\
T'])
def specific_city(country, region, city):
    return 0

@app.route('/load', methods=['POST'])
def load_data():
    return 0

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
