#!/usr/bin/env bash

set -x
docker pull fedora:36
docker build -t fedora-esl:36 .
