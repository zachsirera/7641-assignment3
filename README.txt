Instructions for running code for Zach Sirera's submission to Assignment 3 
CS 7641 - Fall 2020

1.	Clone repository here: https://github.com/zachsirera/7641-assignment3


2. 	run "pip3 install -r requirements.txt" to get all necessary libraries
		

3. 	The analytical portion of the assignment is contained to "analyze.py" where each function does some combination of extracting the dataset, applying a 	DR algorithm and a clustering algorithm, or training the neural netowrk. The outputs are typically printed out to the console, which were then copied and pasted into the "plot.py" file to generate graphs. To reproduce any of the data simply uncomment the relevant section from the "if name == main" section. 


4.	All graph generation is handled in "plot.py". 
	Running plot.py will generate all of the graphs that are used in the report. 
	With the exception of a couple that were easier to generate in analyze.py, such as the neural detwork graphs or the 2/3D component visualization graphs.
	The data in plot.py is self-contained. You do not need to run analyze.py to get it. It was copied and pasted into plot.py as needed. 
