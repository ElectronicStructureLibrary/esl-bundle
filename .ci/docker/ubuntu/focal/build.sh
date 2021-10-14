#!/usr/bin/env bash

set -x

docker pull ubuntu:focal
docker build -t ubuntu-esl:focal .
