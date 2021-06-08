#!/usr/bin/env bash

set -x
docker pull fedora:34
docker build -t fedora-esl:34 .
