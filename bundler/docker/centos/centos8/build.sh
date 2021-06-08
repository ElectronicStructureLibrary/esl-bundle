#!/usr/bin/env bash

set -x
docker pull centos:8
docker build -t centos-esl:8 .
