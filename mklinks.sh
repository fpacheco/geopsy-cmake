#!/bin/bash
for d in $(ls -d ../*/) 
do
  dd="${d:3:-1}"
  echo "$dd"
  if [ "$dd" != "geopsy-cmake" ]; then
    ln -s $d geopsy-$dd
  fi
done
