#/bin/bash

echo "$0 is RUNNING"

echo "Do thing here"
echo "and here"

echo "This is argument #1 => $1"

if [[ "$1" == "andrew" ]]; then
  echo "Hi ANDREW!"
fi

echo "$0 is STOPPING"
