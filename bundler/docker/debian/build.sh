#!/usr/bin/env bash

set -x

docker pull debian:buster
docker build -t debian-esl:buster . 
