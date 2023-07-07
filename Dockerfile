FROM python:3.11-slim
COPY . /var/nijikabot/
WORKDIR /var/nijikabot
RUN pip install --upgrade pip && pip install .