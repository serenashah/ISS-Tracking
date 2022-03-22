# ISS Data Querier
This project offers users the ability to sift through abundant amounts of data  about the International Space Station (ISS) and easily access specific information about the ISS (including its position, velocity, and various sightings across the world) using a containerized Flask web application. 
#### This repository includes:
- ```iss_tracking_app.py```: the Flask web application that returns routes with information about the ISS
- ```test_iss.py```: a test suite for the functions of the application
- ```Dockerfile```: a text document with commands for user to assemble a Docker container with the app's required dependencies
- ```Makefile```: a file that can be executed to perform the tasks of building, running, and pushing the container
#### Supplemental files of interest:
- - ```ISS.OEM_J2K_EPH.xml```: an XML file with positional data, including abundant informtion about the ISS's position and velocity at a given epoch
- ```XMLsightingData_citiesUSA07.xml```: an XML file with sighting data, including abundant information about the ISS's local sightings in the United States
