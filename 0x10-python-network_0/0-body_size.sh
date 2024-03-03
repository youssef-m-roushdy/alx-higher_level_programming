#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a request to the URL and store the response in a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$1"

# Get the size of the response body in bytes
response_size=$(wc -c < "$response_file")

# Display the size of the response body
echo "Size of the response body: $response_size bytes"

# Clean up the temporary file
rm "$response_file"
