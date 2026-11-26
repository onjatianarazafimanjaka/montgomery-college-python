#!/bin/bash
echo 'Hello '$1'!'
echo '$1 is all the money you have.'
echo "Surely $1 has more money than that!"

if [ -n "$2" ]; then
    echo "$2 chimed in."
else
    echo "Nobody said anything."
fi
