FROM python:3.8-slim

WORKDIR /app

COPY MainScore.py /app

COPY Utils.py /app

RUN mkdir /app/templates

COPY Utils.py /app

COPY templates/error.html /app/templates

COPY templates/score.html /app/templates

RUN pip install flask

RUN pip install selenium

EXPOSE 5000

VOLUME /app/data

CMD ["python", "MainScore.py"]
