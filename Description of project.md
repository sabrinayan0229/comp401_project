
# Creation of Python Script 
## C.Elegan Angle and Orientation Calculation
#### File name: read.py

#### Purpose:
Filter our the likelihood of 3 main points of the C.elegans and find the angle between 3 coordinates. Calculate the worm orientations which can then be used for future steps in analysis.

#### Input:
An excel sheet of 8 points' x,y coordinates and likelihood. This should be in the same folder as this python script, using the command line: "python3 readdata.py #INPUT_FILE " 

#### Output:
An excel file with x and y coordinates of all points that meet the conditions, calculated angle and orientation (left or right). 


##### References
library used: numpy, math, panda