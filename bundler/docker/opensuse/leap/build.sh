#!/usr/bin/env bash

set -x

docker -l debug build -t opensuse-esl:leap-15.2 . 
