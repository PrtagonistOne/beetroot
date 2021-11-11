FROM python:3.9.7-slim

ARG WORKDIR=/wd
WORKDIR ${WORKDIR}

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade --requirement ./requirments.txt

COPY ./run_app.py ./run_app.py
COPY ./app ./app
COPY ./config ./config

ENTRYPOINT ["python"]

CMD ["python","/wd/run_app.py"]