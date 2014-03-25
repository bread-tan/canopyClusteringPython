#! /usr/bin/env bash

# Configuration variables
BASEFOLDER=/tmp/pmaxT
DATAPOINTSFILE=dataPoints.txt

# Generated variables
DATASET=$BASEFOLDER/input/$DATAPOINTSFILE

CANOPYCENTERFOLDER=$BASEFOLDER/output1
CANOPYCENTERFILE=CANOPYCENTERFOLDER/part-00000

CANOPYASSIGNFOLDER=$BASEFOLDER/output2
CANOPYASSIGNFILE=$CANOPYASSIGNFOLDER/part-00000

hadoop dfs -rmr $BASEFOLDER/output2

COUNTER=0

step3(){
	COUNTER=`expr $COUNTER + 1`
	cat canopyAssign.txt | ./mapperStg3.py canopyCenters.txt $1 | sort | ./reducerStg3.py > kCentroids_$COUNTER.txt
	./test.py $1 kCentroids_$COUNTER.txt
}

# Stage 1
# hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
# -input $DATASET \
# -output $CANOPYCENTERFOLDER \
# -file DataPoint.py \
# -file mapperStg1.py \
# -file reducerStg1.py \
# -mapper mapperStg1.py \
# -reducer reducerStg1.py

# Stage 2
hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
-input $DATASET \
-output $CANOPYASSIGNFOLDER \
-file DataPoint.py \
-file mapperStg2.py \
-file reducerStg2.py \
-mapper "mapperStg2.py $CANOPYCENTERFILE" \
-reducer reducerStg2.py
#cat dataPoints.txt | ./mapperStg2.py | sort | ./reducerStg2.py > canopyAssign.txt

# # Stage 3
# step3 kCentroids.txt
# while [ $? -eq 0 ]; do
# 	step3 kCentroids_$COUNTER.txt
# done

# cp kCentroids_$COUNTER.txt kCentroidsFinal.txt

# # Stage 4
# cat dataPoints.txt | ./mapperStg4.py kCentroidsFinal.txt | sort | ./reducerStg4.py > outputz
