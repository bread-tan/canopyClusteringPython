Canopy Clustering using MapReduce in Hadoop
=

Files Included:
-
<ul>
	<li><b>Gen.py</b></li>
	<li><b>Stage 1: Canopy Center<b>
		<ul>
			<li>mapperStg1.py</li> 
			<li>reducerStg1.py</li>
		</ul>
	</li>
	<li><b>Stage 2: Canopy Assign<b>
		<ul>
			<li>mapperStg2.py</li>
			<li>reducerStg2.py</li>
		</ul>
	</li>
	<li><b>Stage 3: Cluster Center<b>
		<ul>
			<li>mapperStg3.py</li>
			<li>reducerStg3.py</li>
		</ul>
	</li>
	<li><b>Stage 4: Cluster Assign:</b>
		<ul>
			<li>mapperStg4.py</li>
			<li>reducerStg4.py</li>
		</ul>
	</li>
</ul>


#Functions of each of the files will be updated at a later date.#


Description of the files:
=

Gen.py
-
-> Generates the Data Set on which we use Canopy-Clustering.
-> Generates a set of k-Centroids.

DataPoint.py
-
-> DataPoint class.

Stage 1: Canopy Center
-
<ul>
	<li>Mapper:</li>
		<ul>
			<li>Input: Data points.</li>
			<li>Output: List of Canopy Centers.</li>
			<li>Function: </li>
		</ul>
	<li>Reducer:</li>
		<ul>
			<li>Input: Canopy Centers</li>
			<li>Output: Canopy Centers</li>
			<li>Function: </li>
		</ul>
</ul>

Stage 2: Canopy Assign
-
<ul>
	<li>Mapper:</li>
		<ul>
			<li>Input: Canopy Centers </li>
			<li>Output: Canopy Centers and the Data Points that belong to each.</li>
			<li>Function: </li>
		</ul>
	<li>Reducer:</li>
		<ul>
			<li>Input: Canopy Centers, Data Points (stdin)</li>
			<li>Output: Identity </li>
			<li>Function: Echos the result from the Mapper.</li>
		</ul>
</ul>

Stage 3: Cluster Center
-
<ul>
	<li>Mapper:</li>
		<ul>
			<li>Input: </li>
				<ul>-> List of 'k' Centroids</ul>
				<ul>-> List of Canopy Centers</ul>
				<ul>-> Canopy Centers, Data Points (stdin)</ul>
			<li>Output: K Centroids and the Data Points that belong to each. </li>
			<li>Function: </li>
		</ul>
	<li>Reducer:</li>
		<ul>
			<li>Input: </li>
			<li>Output: </li>
			<li>Function: </li>
		</ul>
</ul>

Stage 4: Cluster Assign
-
<ul>
	<li>Mapper:</li>
		<ul>
			<li>Input: </li>
			<li>Output: </li>
			<li>Function: </li>
		</ul>
	<li>Reducer:</li>
		<ul>
			<li>Input: </li>
			<li>Output: </li>
			<li>Function: </li>
		</ul>
</ul>



To replicate running:
-

Edit the run.sh shell script to run.

Note: 
+ If running on windows cmd, you have to create your own Sort function to sort input from the mapper. 
+ Personally, I'd recommend just using a linux OS to smoothen it all out.
