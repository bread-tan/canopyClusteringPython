#! /usr/bin/env bash

rm kCentroids_*
rm canopyCenters.txt
rm canopyAssign.txt

COUNTER=0

step3()
{
	COUNTER=`expr $COUNTER + 1`
	cat canopyAssign.txt | ./mapperStg3.py canopyCenters.txt $1 | sort | ./reducerStg3.py > kCentroids_$COUNTER.txt
	./test.py $1 kCentroids_$COUNTER.txt
}

# Stage 1
cat dataPoints.txt | ./mapperStg1.py | sort | ./reducerStg1.py > canopyCenters.txt

# Stage 2
cat dataPoints.txt | ./mapperStg2.py | sort | ./reducerStg2.py > canopyAssign.txt

# Stage 3
step3 kCentroids.txt
while [ $? -eq 0 ]; do
	step3 kCentroids_$COUNTER.txt
done

cp kCentroids_$COUNTER.txt kCentroidsFinal.txt

# Stage 4
cat dataPoints.txt | ./mapperStg4.py kCentroidsFinal.txt | sort | ./reducerStg4.py > outputz