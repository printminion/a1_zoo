#FROM python:3.7.2-alpine
FROM amancevice/pandas:0.24.1-slim

LABEL maintainer="m.kupriyanov@gmail.com"

RUN apt-get update \
&& apt-get install -y make curl \
&& rm -rf /var/lib/apt/lists/*


RUN mkdir /code/
ADD requirements.txt /code/requirements.txt

WORKDIR /code
RUN pip install -r requirements.txt


ADD . /code


CMD [ "python", "calculate.py -h" ]