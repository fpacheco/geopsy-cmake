#!/bin/bash
G_SRCS="geopsy-src" 
mkdir $G_SRCS
for d in $(ls -d ../*/) 
do
  dd="${d:3:-1}"
  echo "$dd"
  if [ "$dd" != "geopsy-cmake" ]; then
    ln -s ../$d $G_SRCS/$dd
  fi
done
