FROM python:3.6

RUN pip install flask==1.1.1
COPY main.py /main.py
