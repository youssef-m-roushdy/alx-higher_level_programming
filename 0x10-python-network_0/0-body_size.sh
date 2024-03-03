#!/bin/bash
URL=$1
res=$(curl -sI $URL | grep -i content-length)
echo "$res"