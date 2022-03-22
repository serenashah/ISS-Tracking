# ISS Data Querier
This project offers users the ability to sift through abundant amounts of data  about the International Space Station (ISS) and easily access specific information about the ISS (including its position, velocity, and various sightings across the world) using a containerized Flask web application. 
#### This repository includes:
- ```iss_tracking_app.py```: the Flask web application that returns routes with information about the ISS
- ```test_iss.py```: a test suite for the functions of the application
- ```Dockerfile```: a text document with commands for user to assemble a Docker container with the app's required dependencies
- ```Makefile```: a file that can be executed to perform the tasks of building, running, and pushing the container
#### Supplemental files necessary:
- ```ISS.OEM_J2K_EPH.xml```: an XML file with positional data, including abundant informtion about the ISS's position and velocity at a given epoch
- ```XMLsightingData_citiesUSA07.xml```: an XML file with sighting data, including abundant information about the ISS's local sightings in the United States

## Datasets
The XML files mentioned above are datasets provided by NASA's Johnson Space Center, updated February 13, 2022. For the application to access these files, download them into a directory with the files included in this repository. 
You can download both the positional data and sighting data at this [link](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq) under the names **Public Distribution File** and **XMLsightingData_citiesUSA07**, respectively.
You can also download them into your directory in terminal with the ```wget```:
```bash
[user@f5p~]$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml
[user@f5p~]$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA07.xml
ISS.OEM_J2K_EPH.xml  100%[======================>]   2.83M  1.03MB/s    in 2.8s
XMLsightingData_citi 100%[======================>]   1.80M  1.04MB/s    in 1.7s
