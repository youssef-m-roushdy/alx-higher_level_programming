#!/bin/bash

# Check if the user provided a URL
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL using curl and store the response body in a variable
response=$(curl -s "$1")

# Calculate the size of the response body in bytes
size=$(echo -n "$response" | wc -c)

# Display the size of the response body in bytes
echo "$size"
