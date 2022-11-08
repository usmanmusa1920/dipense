FROM python:3.8.5-alpine

LABEL name="dipense"
LABEL version="test"
LABEL description="An OSINT tool lab for IT ninjas"
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

