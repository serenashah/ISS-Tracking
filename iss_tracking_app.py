from flask import Flask, request
import xmltodict

app = Flask(__name__)

sighting_data = {}
positional_data = {}

@app.route('/download_data', methods=['POST'])
def download_data():
    
    global sighting_data
    global positional_data

    with open('XMLsightingData_citiesUSA07.xml', 'r') as f:
        sighting_data = xmltodict.parse(f.read())
    
    with open('ISS.OEM_J2K_EPH.xml', 'r') as f:
        positional_data = xmltodict.parse(f.read())
       
    return 'Data has been loaded.\n'

@app.route('/how_to_use', methods=['GET'])
def how_to_use():
    usage_message = 'ISS Tracking App Usage\n'
    return(usage_message)

@app.route('/epochs', methods=['GET'])
def epoch_info():
    epoch_list = {}
    for x in range(len(positional_data)):
        epoch_list['EPOCH'].append(positional_data['ndm']['oem']['body']['segment']['data']['stateVector'][x]['EPOCH'])
    return str(len(positional_data['ndm']['oem']['body']['segment']['data']['stateVector']))

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
