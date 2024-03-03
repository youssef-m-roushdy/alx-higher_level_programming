#!/bin/bash

curl -sI $1 | grep -c Content-Length
