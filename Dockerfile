FROM python:3.8.5-alpine

RUN pip install --upgrade pip

RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./dipense /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

