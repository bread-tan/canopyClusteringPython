Canopy Clustering using MapReduce in Hadoop
=

Files Included:
-
<ul>
<li><b>Gen.py</b></li>
<li><b>Stage 1:<b>
<ul><li>MapperStg1.py</li> 
<li>ReducerStg1.py</li></ul>
<li><b>Stage 2:
<ul><li>MapperStg2.py</li>
<li>ReducerStg2.py</li></ul>
</ul>


Functions of each of the files will be updated at a later date.


To replicate running:
-

1) Run gen.py to create the DataSet in dataPoints.txt
2) To get a list of Canopy Centers pipe the files of Stage 1. 
+ + "cat dataPoints.txt | ./mapperStg1.py | sort | ./reducerStg1.py"
+ + + Output will be a list of Canopy Centers stored in canopyCenters.txt
+ + + + Output will be in the format "1\tDataPoint"

3) Pipe that to Stage 2 to assign each data point to a Canopy Center.
+ + Output will be in the format "CanopyCenter\tDataPoint"


Note: 
+ If running on windows cmd, you have to create your own Sort function to sort input from the mapper. 
+ Personally, I'd recommend just using a linux OS to smoothen it all out.
