# first stage build
FROM python:3.7 AS base
# copy requirements
COPY requirements.txt ./
# install requirements
RUN pip install -r requirements.txt
# create app dir
WORKDIR /app
# copy everything to app dir
COPY . /app

RUN chmod +x /app/docker/flask/wait-for-it.sh && chmod +x /app/build.sh

# second stage build
FROM python:3.7-slim AS release
# needed to able run make command
RUN apt-get update && apt-get install make
# set work dir
WORKDIR /app
# copy everything from base
COPY --from=base /app/requirements.txt ./
COPY --from=base /root/.cache /root/.cache
# install requirements
RUN pip install -r requirements.txt
# copy again
COPY --from=base /app ./