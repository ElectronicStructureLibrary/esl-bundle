#!/usr/bin/env bash

set -x

docker pull opensuse/leap:15.3
docker -l debug build -t opensuse-esl:leap-15.3 . 
