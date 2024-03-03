#!/bin/bash

curl -I $1 | grep -i Content-Length
