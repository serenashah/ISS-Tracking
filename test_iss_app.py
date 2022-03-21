from iss_tracking_app import download_data, how_to_use, all_epochs, specific_epoch,\
    all_countries, specific_country, all_regions, specific_region, all_cities, specific_city
import pytest 
    
def how_to_use_test():
    assert isinstance(how_to_use(), str) == True

def specific_epoch_test():
    with pytest.raises(ValueError):
        specific_epoch('hello')

def specfic_country_test():
    with pytest.raises(TypeError):
        specific_country('hello')

def specific_region_test():
    with pytest.raises(TypeError):
        specific_region('hello')

def specific_region_test():
    with pytest.raises(TypeError):
        specific_epoch('hello')
