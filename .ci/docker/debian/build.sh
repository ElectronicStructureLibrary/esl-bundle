#!/usr/bin/env bash

set -x

docker pull debian:bullseye
docker build -t debian-esl:bullseye . 
