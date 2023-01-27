#!/usr/bin/env bash

set -x

docker pull ubuntu:jammy
docker build -t ubuntu-esl:jammy .
