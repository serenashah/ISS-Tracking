from flask import Flask, request
import json
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

download_data()

@app.route('/how_to_use', methods=['GET'])
def how_to_use():
    usage_message = 'ISS Tracking App Usage\n'
    #finish later
    return(usage_message)

@app.route('/epochs', methods=['GET'])
def epoch_info():
    epoch_dict = {}
    number = 0
    for x in positional_data['ndm']['oem']['body']['segment']['data']['stateVector']:
        number += 1
        epoch_dict[f'EPOCH {number}']= x['EPOCH']
    return (json.dumps(epoch_dict, indent=1) + '\n')

@app.route('/epochs/<epoch>', methods=['GET'])
def specific_epoch(epoch: str) -> str:
    epoch_info = positional_data['ndm']['oem']['body']['segment']['data']['stateVector'][int(epoch)-1]
    return (json.dumps(epoch_info, indent=1) + '\n')

@app.route('/countries', methods=['GET'])
def all_countries():
    countries_dict = {}
    number = 0
    for x in sighting_data['visible_passes']['visible_pass']:
        if x['country'] in countries_dict.values():
            number = number
        else:
            number += 1
            countries_dict[f'Country {number}'] = x['country']
    return (json.dumps(countries_dict, indent=1) + '\n')

@app.route('/countries/<country>', methods=['GET'])
def specific_country(country: str) -> str:
    country_info = {}
    country_info_list = []
    for x in sighting_data['visible_passes']['visible_pass']:
        if (country == x['country']):
            country_info_list.append(x)
    country_info[f'{country} Info'] = country_info_list
    return (json.dumps(country_info,indent=1) + '\n')

@app.route('/countries/<country>/regions', methods=['GET'])
def all_regions(country: str) -> str:
    regions_dict = {}
    number = 0
    country_info = json.loads(specific_country(country))
    for x in country_info[f'{country} Info']:
        if x['region'] in regions_dict.values():
            number = number
        else:
            number += 1
            regions_dict[f'Region {number}'] = x['region']
    return (json.dumps(regions_dict, indent=1) + '\n')

@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def specific_region(country: str, region: str) -> str:
    region_info  = {}
    country_info = json.loads(specific_country(country))
    region_info_list = []
    for x in country_info[f'{country} Info']:
        if (region == x['region']):
            region_info_list.append(x)
    region_info[f'{region} Info'] = region_info_list
    return (json.dumps(region_info,indent=1) + '\n')

@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def all_cities(country: str, region: str) -> str:
    cities_dict = {}
    number = 0
    region_info = json.loads(specific_region(country, region))
    for x in region_info[f'{region} Info']:
        if x['city'] not in cities_dict.values():
            number += 1
            cities_dict[f'Cities {number}'] = x['city']
    return (json.dumps(cities_dict, indent=1) + '\n')

@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GE\
T'])
def specific_city(country: str, region: str, city: str) -> str:
    city_info  = {}
    region_info = json.loads(specific_region(country, region))
    city_info_list = []
    for x in region_info[f'{region} Info']:
        if (city == x['city']):
            city_info_list.append(x)
    city_info[f'{city} Info'] = city_info_list
    return (json.dumps(city_info,indent=1) + '\n')

@app.route('/load', methods=['POST'])
def load_data():
    return 0

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
