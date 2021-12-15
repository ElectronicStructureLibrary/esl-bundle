#!/usr/bin/env bash

set -x

#docker pull debian:buster
docker pull debian:bullseye
#docker build -t debian-esl:buster . 
docker build -t debian-esl:bullseye . 
