#! /usr/bin/env bash

# Base folder in HDFS
BASEFOLDER=/tmp/pmaxT

rm kCentroids_*
rm canopyCenters.txt
rm canopyAssign.txt

hadoop dfs -rmr $BASEFOLDER/output*
# 
COUNTER=0

step3(){
	COUNTER=`expr $COUNTER + 1`
	cat canopyAssign.txt | ./mapperStg3.py canopyCenters.txt $1 | sort | ./reducerStg3.py > kCentroids_$COUNTER.txt
	./test.py $1 kCentroids_$COUNTER.txt
}

# Stage 1
hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
-input $BASEFOLDER/input/dataPoints.txt \
-output $BASEFOLDER/output1 \
-file DataPoint.py \
-file mapperStg1.py \
-file reducerStg1.py \
-mapper mapperStg1.py \
-reducer reducerStg1.py

# # Stage 2
# hadoop jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-*.jar \
# -input $BASEFOLDER/input/dataPoints.txt \
# -output $BASEFOLDER/output2 \
# -file DataPoint.py \
# -file mapperStg2.py \
# -file reducerStg2.py \
# -mapper "mapperStg2.py $BASEFOLDER/output1/part-00000" \
# -reducer "reducerStg2.py"
cat dataPoints.txt | ./mapperStg2.py | sort | ./reducerStg2.py > canopyAssign.txt

# # Stage 3
# step3 kCentroids.txt
# while [ $? -eq 0 ]; do
# 	step3 kCentroids_$COUNTER.txt
# done

# cp kCentroids_$COUNTER.txt kCentroidsFinal.txt

# # Stage 4
# cat dataPoints.txt | ./mapperStg4.py kCentroidsFinal.txt | sort | ./reducerStg4.py > outputz