#! /usr/bin/env bash

# Stage 1
cat dataPoints.txt | ./mapperStg1.py | sort | ./reducerStg1.py > canopyCenters.txt

# Stage 2
cat dataPoints.txt | ./mapperStg2.py | sort | ./reducerStg2.py | ./mapperStg3.py
