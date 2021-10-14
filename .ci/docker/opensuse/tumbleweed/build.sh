#!/usr/bin/env bash

set -x

docker pull opensuse/tumbleweed
docker build -t opensuse-esl:tumbleweed .
