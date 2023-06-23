FROM python:3.10.12-alpine

LABEL name="DiPense"
LABEL version="0.1.3"
LABEL description="An OSINT tool for IT ninjas"
MAINTAINER Usman Musa

RUN pip install --upgrade pip

RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./dipense /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
