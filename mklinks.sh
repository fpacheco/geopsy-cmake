#!/bin/bash
for d in $(ls -d ../*/) ; do  ln -s $d geopsy-${d:3:-1}; done
