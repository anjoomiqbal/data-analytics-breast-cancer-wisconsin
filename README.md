In this project some data analytics have been performed on the Breast Cancer Data Set from Wisconsin
URL of data set: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

For this homework 1 the tasks that were performed are briefly discussed below in structures sections. The results can be reproduced by running the following file included in the submission
‘ECE657A-W19-HW1-WisconsinDiagnosticBreastCancerDataAnalysis.py’
 
LIBRARY IMPORTS
	import numpy as np
	import statistics as stat
	from scipy.stats import skew
	from scipy.stats import pearsonr
	import matplotlib.pyplot as plot
 
DATA INPUT
•	The 'breast-cancer-wisconsin.data' file was opened in read-only mode
•	Then the content has been read into python 
•	Then file has been closed

DATA PRE-PROCESSING
•	From the whole file data as string, it has been split into rows 
•	Then each rows have been split into columns
•	Then each element has been converted to integer
•	As the range of all attribute is from 1-10, at this stage missing data attributed have been replaced with integer 0 for easier integer operation of the whole 2D data array or integers
•	Then using numpy library the list has been converted into integer array

DEALING WITH MISSING DATA
•	Missing data fields have been populated with the mode of that column

DATA ANALYSIS
•	Using the statistics and scipy libraries  mean, mode, standard deviation (stdev), variance, skew 
•	Using the pearsonr from scipy libraries, Pearson Correlation Coefficient (PCC) was calculated
•	Using matplotlib.pyplot library, the two histograms were plotted for Clump_Thickness attribute, where one of them is for benign prognosis and the other is for malignant prognosis. 

RESULT PRESENTATION
•	Below are the screenshot reports of the obtained resulting numbers and their meaning
•	For reporting the result values print statements have been used
•	For plotting the histogram the matplotlib.pyplot have been used

 
Task 1 asked to only report the obtained values. 

In task 2 results, we see that all of the attribute have positive PCC with the prognosis of benign or malignant. To compare within them, Mitoses has lower value of PCC compared to Clump Thickness or Bare Nuclei. We can predict the prognosis with higher probability when using the Clump Thickness or Bare Nuclei data compared to using Mitoses data. 
  
For Task 3, we can see from the 2 histograms that based on the value of Clump Thickness we can predict with reasonably high probability whether the prognosis is benign or malignant. E.g. none of the patients with benign prognosis had clump thickness > 8. So if for any new patient clump thickness is measured ≥ 8, then we can predict that there is a very high probability that her prognosis will be malignant. 
Another observation is most patients with Clump Thickness < 5 had a benign prognosis. On the other hand most patients with Clump Thickness > 5 had a malignant prognosis.
The prognosis prediction will be more accurate if multiple attributes are considered together. E.g. based on the past patient’s histogram pattern, if a new patient has test attributes which are all indicating a higher probability of benign prognosis then overall that benign prognosis decision will be much more stronger compared to the case when that decision is just based on a single attribute. 
