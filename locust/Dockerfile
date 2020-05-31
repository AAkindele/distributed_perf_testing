FROM python:3.7

RUN pip install locust
RUN pip install elasticsearch

RUN useradd --create-home --shell /bin/bash locust
USER locust
WORKDIR /home/locust

ADD . .

ENTRYPOINT ["locust"]
