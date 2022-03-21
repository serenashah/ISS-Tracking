from flask import Flask, request
import json
import xmltodict
import logging
import socket

format_str = '%(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format = format_str)

app = Flask(__name__)

@app.route('/download_data', methods=['POST'])
def download_data():
    '''
    Opens and parses two sets of xml data files and loads them into two dictionaries 
    that can be used for all subsequent routes.

    Args: none
    Returns: 
        A string to the client indicating that data has been downloaded.
    '''    
    global sighting_data
    global positional_data

    with open('XMLsightingData_citiesUSA07.xml', 'r') as f:
        sighting_data = xmltodict.parse(f.read())
    
    with open('ISS.OEM_J2K_EPH.xml', 'r') as f:
        positional_data = xmltodict.parse(f.read())


    logging.debug(f'The type of positional_data is {type(positional_data)}')
    logging.debug(f'The type of sighting_data is {type(sighting_data)}')

    return 'Data has been loaded.\n'


@app.route('/how_to_use', methods=['GET'])
def how_to_use():
    '''
    Outputs a message informing the client of the application usage.

    Args: none
    Returns:
        A string message describing application usage.
    '''
    logging.debug('Inside the how_to_use route')

    usage_message = 'ISS Tracking App Usage\n'
    #finish later
    return(usage_message)

@app.route('/epochs', methods=['GET'])
def epoch_info():
    '''
    Reads the positional_data dictionary and creates a dictionary storing all epochs
    in the data.
    
    Args: none
    Returns:
        A dictionary-formatted json string with keys numerating the epochs and values 
        of its corresponding time.
    '''
    logging.debug('Inside the epoch_info route')
    
    epoch_dict = {}
    number = 0
    for x in positional_data['ndm']['oem']['body']['segment']['data']['stateVector']:
        number += 1
        epoch_dict[f'EPOCH {number}']= x['EPOCH']
        
    return (json.dumps(epoch_dict, indent=1) + '\n')

@app.route('/epochs/<epoch>', methods=['GET'])
def specific_epoch(epoch: int) -> str:
    '''
    Given a specific epoch, identified by its integer numberic, outputs all of the 
    given data about the ISS at that epoch.

    Args: 
        epoch (int): epoch sighting identification number
    Returns:
        A dictionary-formatted json string of information about the ISS at the given 
        epoch.
    '''
    logging.debug('Inside the specific_epoch route')

    epoch_info = positional_data['ndm']['oem']['body']['segment']['data']['stateVector']\
        [int(epoch)-1]
    
    return (json.dumps(epoch_info, indent=1) + '\n')

@app.route('/countries', methods=['GET'])
def all_countries():
    '''
    Reads the sighting_data dictionary and creates a dictionary storing all countries 
    in the data.

    Args: none
    Returns:
        A dictionary-formatted json string with keys numerating the countries and 
        values of the different countries in the dict.
    '''
    logging.debug('Inside the all_countries route')

    countries_dict = {}
    number = 0
    for x in sighting_data['visible_passes']['visible_pass']:
        if x['country'] not in countries_dict.values():
            number += 1
            countries_dict[f'Country {number}'] = x['country']

    return (json.dumps(countries_dict, indent=1) + '\n')

@app.route('/countries/<country>', methods=['GET'])
def specific_country(country: str) -> str:
    '''
    Given a specific country outputs all information about the country in the 
    sighting_data.

    Args:
        country (str): name of the country
    Returns:
        A dict-of-list-of-dicts-formatted json string of all the sighting information
        for the given country.
    '''
    logging.debug('Inside the specific_country route')
    country_info = {}
    country_info_list = []
    for x in sighting_data['visible_passes']['visible_pass']:
        if (country == x['country']):
            country_info_list.append(x)
    country_info[f'{country} Info'] = country_info_list

    if len(country_info_list) == 0:
        logging.error('No country with this data.')
    else:
        return (json.dumps(country_info,indent=1) + '\n')

@app.route('/countries/<country>/regions', methods=['GET'])
def all_regions(country: str) -> str:
    '''
    Reads the sighting_data dictionary and creates a dictionary storing all regions 
    in the data given its country.

    Args: 
        country (str): name of the country
    Returns:
        A dictionary-formatted json string with keys numerating the regions and 
        values of the different regions in the dict.
    '''
    logging.debug('Inside the all_regions route')

    regions_dict = {}
    number = 0
    country_info = json.loads(specific_country(country))
    for x in country_info[f'{country} Info']:
        if x['region'] not in regions_dict.values():
            number += 1
            regions_dict[f'Region {number}'] = x['region']
    return (json.dumps(regions_dict, indent=1) + '\n')

@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def specific_region(country: str, region: str) -> str:
    '''
    Given a specific region of a specific country outputs all information about the 
    city in the sighting_data.

    Args:
        country (str): name of the country
        region (str): name of the region
    Returns:
        A dict-of-list-of-dicts-formatted json string of all the sighting information
        for the given region. 
    ''' 
    logging.debug('Inside the specific_region route')
    
    region_info  = {}
    country_info = json.loads(specific_country(country))
    region_info_list = []
    for x in country_info[f'{country} Info']:
        if (region == x['region']):
           region_info_list.append(x)
    region_info[f'{region} Info'] = region_info_list

    if len(region_info_list) == 0:
        logging.error('No region with this data.')
    else:
        return (json.dumps(region_info,indent=1) + '\n')

@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def all_cities(country: str, region: str) -> str:
    '''
    Reads the sighting_data dictionary and creates a dictionary storing all cities 
    in the data for a given country and region.

    Args: none
    Returns:
        A dictionary-formatted json string with keys numerating the regions and 
        values of the different regions in the dict.
    '''
    logging.debug('Inside the all_cities route')

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
    '''
    Given a specific city in a given country and region, outputs all information 
    about the city in the sighting_data.

    Args:
        country (str): name of the country
        region (str): name of the region
    Returns:
        A dict-of-list-of-dicts-formatted json string of all the sighting information
        for the given city.
    '''
    logging.debug('Inside the specific_city route')

    city_info  = {}
    region_info = json.loads(specific_region(country, region))
    city_info_list = []
    for x in region_info[f'{region} Info']:
        if (city == x['city']):
            city_info_list.append(x)
    city_info[f'{city} Info'] = city_info_list

    if len(city_info_list) == 0:
        logging.error('No city with this data.')
    else:
        return (json.dumps(city_info,indent=1) + '\n')

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
