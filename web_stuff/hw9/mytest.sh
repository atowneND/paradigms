#!/bin/bash

python main.py &
echo "Continue?"
read

port=40092

echo "MOVIES:"
echo "Gets:"
curl -X GET localhost:$port/movies/
curl -X GET localhost:$port/movies/95
echo ""
echo "Deletes:"
curl -X DELETE localhost:$port/movies/
curl -X DELETE localhost:$port/movies/95
echo ""
echo "Put:"
curl -X PUT -H "Content-Type: text/plain" -d'{"value": "4"}' localhost:$port/movies/95
echo ""
echo "Post:"
curl -X POST -H "Content-Type: text/plain" -d'{"value": "4", "key":"95"}' localhost:$port/movies/
echo ""
echo ""

echo "RESET:"
echo "Put:"
curl -X PUT -H "Content-Type: text/plain" -d'{"value": "4"}' localhost:$port/reset/95
echo ""
echo "Put all:"
curl -X PUT -H "Content-Type: text/plain" -d'{"value": "4", "key":"95"}' localhost:$port/reset/
echo ""
echo ""

echo "USERS:"
echo "Gets:"
curl -X GET localhost:$port/users/
curl -X GET localhost:$port/users/95
echo ""
echo "Deletes:"
curl -X DELETE localhost:$port/users/
curl -X DELETE localhost:$port/users/95
echo ""
echo "Put:"
curl -X PUT -H "Content-Type: text/plain" -d'{"value": "4"}' localhost:$port/users/95
echo ""
echo "Post:"
curl -X POST -H "Content-Type: text/plain" -d'{"value": "4", "key":"95"}' localhost:$port/users/
echo ""
echo ""
