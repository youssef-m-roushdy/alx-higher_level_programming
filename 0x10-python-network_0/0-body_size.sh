#!/bin/bash

curl -I $1 | grep -c Content-Length
