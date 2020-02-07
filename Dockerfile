FROM python:3.6-stretch
RUN apt update
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
ENV PORT 8080
RUN ./setup_config_from_env.py
RUN cd api
CMD ["gunicorn", "api:app", "--config=api/gunicorn_config.py"]
