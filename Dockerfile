FROM python:3.6-stretch
RUN apt update
ADD requirements.txt /brainwriting/requirements.txt
RUN pip install -r /brainwriting/requirements.txt
ADD . /brainwriting
EXPOSE 8080
WORKDIR /brainwriting/api
CMD ["gunicorn", "api:app", "--config=gunicorn_config.py"]
