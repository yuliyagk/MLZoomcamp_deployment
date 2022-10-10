FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv
RUN pip install flask

WORKDIR /app
COPY ["model1.bin", "dv.bin", "./"]
