#! /usr/bin/env bash

# Configuration variables
BASEFOLDER=/tmp/pmaxT
DATAPOINTSFILE=dataPoints.txt

# Generated variables
DATASET=$BASEFOLDER/input/$DATAPOINTSFILE
KCENTROIDSFILE=$BASEFOLDER/input/centroids.txt

CANOPYCENTERFOLDER=$BASEFOLDER/output1
CANOPYCENTERFILE=$CANOPYCENTERFOLDER/part-00000

CANOPYASSIGNFOLDER=$BASEFOLDER/output2
CANOPYASSIGNFILE=$CANOPYASSIGNFOLDER/part-00000

CLUSTERCENTERFOLDER=$BASEFOLDER/output3_

CLUSTERASSIGNFOLDER=$BASEFOLDER/output4

# Cleanup HDFS
hadoop dfs -rmr $BASEFOLDER/output*

# Counter for number of iterations
COUNTER=0

step3(){
	COUNTER=`expr $COUNTER + 1`

	hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
	-input $CANOPYASSIGNFILE \
	-output $CLUSTERCENTERFOLDER$COUNTER \
	-file DataPoint.py \
	-file mapperStg3.py \
	-file reducerStg3.py \
	-mapper "mapperStg3.py $CANOPYCENTERFILE $1" \
	-reducer reducerStg3.py

	./compareCentroids.py $1 $CLUSTERCENTERFOLDER$COUNTER/part-00000
}

# Stage 1
hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
-input $DATASET \
-output $CANOPYCENTERFOLDER \
-file DataPoint.py \
-file mapperStg1.py \
-file reducerStg1.py \
-mapper mapperStg1.py \
-reducer reducerStg1.py

# Stage 2
hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
-input $DATASET \
-output $CANOPYASSIGNFOLDER \
-file DataPoint.py \
-file mapperStg2.py \
-file reducerStg2.py \
-mapper "mapperStg2.py $CANOPYCENTERFILE" \
-reducer reducerStg2.py

# Stage 3
step3 $KCENTROIDSFILE
while [ $? -eq 0 ]; do
	step3 $CLUSTERCENTERFOLDER$COUNTER/part-00000
done

# Stage 4
hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
-input $DATASET \
-output $CLUSTERASSIGNFOLDER \
-file DataPoint.py \
-file mapperStg4.py \
-file reducerStg4.py \
-mapper "mapperStg4.py $CLUSTERCENTERFOLDER$COUNTER/part-00000" \
-reducer reducerStg4.py