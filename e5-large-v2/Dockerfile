FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

RUN apt update
RUN apt install -y python3 python3-pip

WORKDIR /app

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./preload.py ./
RUN python3 preload.py

COPY ./main.py ./
ENTRYPOINT uvicorn main:app --host=0.0.0.0 --port=80