FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install pytest==7.0.0
RUN pip3 install --user xmltodict
RUN pip3 install --user Flask==2.0.3

RUN mkdir /iss_app
WORKDIR /iss_app
COPY iss_tracking_app.py /iss_app
COPY XMLsightingData_citiesUSA07.xml /iss_app
COPY ISS.OEM_J2K_EPH.xml /iss_app
COPY test_iss_app.py /iss_app

ENTRYPOINT ["python3"]
CMD ["iss_tracking_app.py"]