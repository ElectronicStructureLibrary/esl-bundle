#!/usr/bin/env bash

set -x

docker pull ubuntu:bionic
docker build -t ubuntu-esl:bionic .
