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

## Installation
Clone this repository onto your desktop with 
```bash
[user@f5p~]$ git clone https://github.com/serenashah/iss-tracking.git
```
### Data Sets
The XML files mentioned above are datasets provided by NASA's Johnson Space Center, updated February 13, 2022. For the application to access these files, download them into your local repository with the files included in this repository.  

You can download both the positional data and sighting data at this [link](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq) under the names '**Public Distribution File**' and '**XMLsightingData_citiesUSA07**', respectively.   
You can also download them into your directory in terminal with ```wget```:
```bash
[user@f5p~]$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml 
[user@f5p~]$ wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA07.xml 
```
## Usage 
### Docker 
The ```Dockerfile``` containerizes the Flask web server, creating a microservice with which you can interact and containing all the dependencies and environment requirements needed to utilize the application. 
#### Using the Makefile
The included ```Makefile``` and running the Docker image in the background can be done easily with ```make```:
```bash
[user@f5p~]$ make all
docker build -t f5p/flask-iss-app:latest .
[+] Building 8.1s (16/16) FINISHED
...
541be2ee1a378ac6e62f5336c49f99651e5028d6a15441c4a9cf1867405b11c3
```
#### Building and running manually
Alternatively, you can manually build and run the containerized app with:
```bash
[user@f5p~]$ docker build -t serenashah/flask-iss-app:latest .
docker build -t f5p/flask-iss-app:latest .
[+] Building 8.1s (16/16) FINISHED
[user@f5p~]$ docker run --name "<container-name>" -d -p 5028:5000 --rm -v serenashah/flask-iss-app:latest
541be2ee1a378ac6e62f5336c49f99651e5028d6a15441c4a9cf1867405b11c3
```
#### Checking status and stopping
To see if your container is up and running, check that the status of your container is ```Up```.
```bash
[user@f5p~]$ docker ps -a
CONTAINER ID   IMAGE    ..................  CREATED         STATUS     
541be2ee1a37   f5p/flask-iss-app:latest     4 minutes ago   Up 4 minutes       
```
Once you've finished using the application, stop your container with:
```bash
[user@f5p~]$ docker stop <CONTAINER ID>
<CONTAINER ID>
```
#### Pulling a pre-containerized copy
You may also pull a copy of an existing pre-containerized application from Docker Hub with the following command:
```bash
[user@f5p~]$ docker pull serenashah/flask-iss-app:latest
```
### App 
### Test Suite 
