FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install pytest==7.0.0

RUN pip3 install --user xmltodict

COPY iss_tracking_app.py /code/iss_tracking_app.py

ENV PATH "/code:$PATH"