 # Number of Instances: 699 (as of 15 July 1992)
 # Number of Attributes: 10 plus the class attribute
 # Attribute Information: (class attribute has been moved to last column)

   # #  Attribute                     Domain
   # -- -----------------------------------------
   # 1. Sample code number            id number
   # 2. Clump Thickness               1 - 10
   # 3. Uniformity of Cell Size       1 - 10
   # 4. Uniformity of Cell Shape      1 - 10
   # 5. Marginal Adhesion             1 - 10
   # 6. Single Epithelial Cell Size   1 - 10
   # 7. Bare Nuclei                   1 - 10
   # 8. Bland Chromatin               1 - 10
   # 9. Normal Nucleoli               1 - 10
  # 10. Mitoses                       1 - 10
  # 11. Class:                        (2 for benign, 4 for malignant)

 # Missing attribute values: 16
   # There are 16 instances in Groups 1 to 6 that contain a single missing 
   # (i.e., unavailable) attribute value, now denoted by "?".

import numpy as np
import statistics as stat
from scipy.stats import skew
from scipy.stats import pearsonr
import matplotlib.pyplot as plot
   
############################################
################ DATA INPUT  
############################################

filename = 'breast-cancer-wisconsin.data'
file = open (filename, mode='r')
data = file.read()
file.close()

############################################
################ DATA PRE-PROCESSING 
############################################

## converting the whole data into rows
data = data.split('\n')

## deleting the last row as it is empty
del data[len(data)-1]

num_of_rows = (len(data))

## converting each row of data into columns
for i in range(0, num_of_rows):
    data[i]=data[i].split(',')

num_of_cols = (len(data[0]))

## converting each string element to int
## MISSING DATA are represented as '?', so we are not converting them
for i in range(0, num_of_rows):
    for j in range(0, num_of_cols):
        if data[i][j] != '?':
            data[i][j] = int(data[i][j])
        else:
            data[i][j] = int(0)

data=np.array(data)

mode_Clump_Thickness 			= int(stat.mode(data[:,1]))
mode_Uniformity_of_Cell_Size 		= int(stat.mode(data[:,2]))
mode_Uniformity_of_Cell_Shape 		= int(stat.mode(data[:,3]))
mode_Marginal_Adhesion 			= int(stat.mode(data[:,4]))
mode_Single_Epithelial_Cell_Size 	= int(stat.mode(data[:,5]))
mode_Bare_Nuclei 			= int(stat.mode(data[:,6]))
mode_Bland_Chromatin 		        = int(stat.mode(data[:,7]))
mode_Normal_Nucleoli 			= int(stat.mode(data[:,8]))
mode_Mitoses 				= int(stat.mode(data[:,9]))

############################################
################ DEALING WITH MISSING DATA
############################################
# Assuming '?' will not be the mode of any attribute
# filling in missing data with the mode of t hat column
for i in range(0, num_of_rows):
    for j in range(0, num_of_cols):
        if data[i][1] == 0:
            data[i][1] = mode_Clump_Thickness
        if data[i][2] == 0:
            data[i][2] = mode_Uniformity_of_Cell_Size
        if data[i][3] == 0:
            data[i][3] = mode_Uniformity_of_Cell_Shape
        if data[i][4] == 0:
            data[i][4] = mode_Marginal_Adhesion
        if data[i][5] == 0:
            data[i][5] = mode_Single_Epithelial_Cell_Size
        if data[i][6] == 0:
            data[i][6] = mode_Bare_Nuclei
        if data[i][7] == 0:
            data[i][7] = mode_Bland_Chromatin
        if data[i][8] == 0:
            data[i][8] = mode_Normal_Nucleoli
        if data[i][9] == 0:
            data[i][9] = mode_Mitoses
	

############################################
################ DATA ANALYSIS 
############################################
# Task 1
mean_Clump_Thickness 		    = stat.mean(data[:,1])
mean_Uniformity_of_Cell_Size 	    = stat.mean(data[:,2])
mean_Uniformity_of_Cell_Shape 	    = stat.mean(data[:,3])
mean_Marginal_Adhesion 		    = stat.mean(data[:,4])
mean_Single_Epithelial_Cell_Size    = stat.mean(data[:,5])
mean_Bare_Nuclei 		    = stat.mean(data[:,6])
mean_Bland_Chromatin 		    = stat.mean(data[:,7])
mean_Normal_Nucleoli 		    = stat.mean(data[:,8])
mean_Mitoses 			    = stat.mean(data[:,9])

stdev_Clump_Thickness 		    = stat.stdev(data[:,1])
stdev_Uniformity_of_Cell_Size 	    = stat.stdev(data[:,2])
stdev_Uniformity_of_Cell_Shape 	    = stat.stdev(data[:,3])
stdev_Marginal_Adhesion 	    = stat.stdev(data[:,4])
stdev_Single_Epithelial_Cell_Size   = stat.stdev(data[:,5])
stdev_Bare_Nuclei 		    = stat.stdev(data[:,6])
stdev_Bland_Chromatin 		    = stat.stdev(data[:,7])
stdev_Normal_Nucleoli 		    = stat.stdev(data[:,8])
stdev_Mitoses 			    = stat.stdev(data[:,9])

variance_Clump_Thickness 	    = stat.variance(data[:,1])
variance_Uniformity_of_Cell_Size    = stat.variance(data[:,2])
variance_Uniformity_of_Cell_Shape   = stat.variance(data[:,3])
variance_Marginal_Adhesion 	    = stat.variance(data[:,4])
variance_Single_Epithelial_Cell_Size= stat.variance(data[:,5])
variance_Bare_Nuclei 		    = stat.variance(data[:,6])
variance_Bland_Chromatin 	    = stat.variance(data[:,7])
variance_Normal_Nucleoli 	    = stat.variance(data[:,8])
variance_Mitoses 		    = stat.variance(data[:,9])

skew_Clump_Thickness 		    = skew(data[:,1])
skew_Uniformity_of_Cell_Size 	    = skew(data[:,2])
skew_Uniformity_of_Cell_Shape 	    = skew(data[:,3])
skew_Marginal_Adhesion 	            = skew(data[:,4])
skew_Single_Epithelial_Cell_Size    = skew(data[:,5])
skew_Bare_Nuclei 		    = skew(data[:,6])
skew_Bland_Chromatin 		    = skew(data[:,7])
skew_Normal_Nucleoli 		    = skew(data[:,8])
skew_Mitoses 			    = skew(data[:,9])

# Task 2
pearsonr_prognosis_vs_Clump_Thickness 		    = pearsonr(data[:,10], data[:,1])
pearsonr_prognosis_vs_Uniformity_of_Cell_Size 	    = pearsonr(data[:,10], data[:,2])
pearsonr_prognosis_vs_Uniformity_of_Cell_Shape 	    = pearsonr(data[:,10], data[:,3])
pearsonr_prognosis_vs_Marginal_Adhesion 	    = pearsonr(data[:,10], data[:,4])
pearsonr_prognosis_vs_Single_Epithelial_Cell_Size   = pearsonr(data[:,10], data[:,5])
pearsonr_prognosis_vs_Bare_Nuclei 		    = pearsonr(data[:,10], data[:,6])
pearsonr_prognosis_vs_Bland_Chromatin 		    = pearsonr(data[:,10], data[:,7])
pearsonr_prognosis_vs_Normal_Nucleoli 		    = pearsonr(data[:,10], data[:,8])
pearsonr_prognosis_vs_Mitoses 			    = pearsonr(data[:,10], data[:,9])

# Task 3
bin_benign =[]
bin_malignant =[]
for i in range(0, num_of_rows):
    if data[i][10] == 2:
        bin_benign.append(data[i][1])       # for histogram of Clump_Thickness
    else:
        bin_malignant.append(data[i][1])    # for histogram of Clump_Thickness

############################################
################ RESULT PRESENTATION 
############################################
print ('---------------------------------------------------')
print ('TASK 1')
print ('---------------------------------------------------')
print ('mean_Clump_Thickness = ', 	        mean_Clump_Thickness)
print ('mean_Uniformity_of_Cell_Size = ', 	mean_Uniformity_of_Cell_Size)
print ('mean_Uniformity_of_Cell_Shape = ',      mean_Uniformity_of_Cell_Shape)
print ('mean_Marginal_Adhesion = ', 		mean_Marginal_Adhesion)
print ('mean_Single_Epithelial_Cell_Size = ',   mean_Single_Epithelial_Cell_Size)
print ('mean_Bare_Nuclei = ', 			mean_Bare_Nuclei)
print ('mean_Bland_Chromatin = ', 		mean_Bland_Chromatin)
print ('mean_Normal_Nucleoli = ', 		mean_Normal_Nucleoli)
print ('mean_Mitoses = ', 			mean_Mitoses)
print ('---------------------------------------------------')
print ('mode_Clump_Thickness = ', 	        mode_Clump_Thickness)
print ('mode_Uniformity_of_Cell_Size = ', 	mode_Uniformity_of_Cell_Size)
print ('mode_Uniformity_of_Cell_Shape = ',      mode_Uniformity_of_Cell_Shape)
print ('mode_Marginal_Adhesion = ', 		mode_Marginal_Adhesion)
print ('mode_Single_Epithelial_Cell_Size = ',   mode_Single_Epithelial_Cell_Size)
print ('mode_Bare_Nuclei = ', 			mode_Bare_Nuclei)
print ('mode_Bland_Chromatin = ', 		mode_Bland_Chromatin)
print ('mode_Normal_Nucleoli = ', 		mode_Normal_Nucleoli)
print ('mode_Mitoses = ', 			mode_Mitoses)
print ('---------------------------------------------------')
print ('stdev_Clump_Thickness = ', 	        stdev_Clump_Thickness)
print ('stdev_Uniformity_of_Cell_Size = ', 	stdev_Uniformity_of_Cell_Size)
print ('stdev_Uniformity_of_Cell_Shape = ',     stdev_Uniformity_of_Cell_Shape)
print ('stdev_Marginal_Adhesion = ', 		stdev_Marginal_Adhesion)
print ('stdev_Single_Epithelial_Cell_Size = ',  stdev_Single_Epithelial_Cell_Size)
print ('stdev_Bare_Nuclei = ', 			stdev_Bare_Nuclei)
print ('stdev_Bland_Chromatin = ', 		stdev_Bland_Chromatin)
print ('stdev_Normal_Nucleoli = ', 		stdev_Normal_Nucleoli)
print ('stdev_Mitoses = ', 			stdev_Mitoses)
print ('---------------------------------------------------')
print ('variance_Clump_Thickness = ', 	            variance_Clump_Thickness)
print ('variance_Uniformity_of_Cell_Size = ', 	    variance_Uniformity_of_Cell_Size)
print ('variance_Uniformity_of_Cell_Shape = ',      variance_Uniformity_of_Cell_Shape)
print ('variance_Marginal_Adhesion = ', 	    variance_Marginal_Adhesion)
print ('variance_Single_Epithelial_Cell_Size = ',   variance_Single_Epithelial_Cell_Size)
print ('variance_Bare_Nuclei = ', 		    variance_Bare_Nuclei)
print ('variance_Bland_Chromatin = ', 		    variance_Bland_Chromatin)
print ('variance_Normal_Nucleoli = ', 		    variance_Normal_Nucleoli)
print ('variance_Mitoses = ', 			    variance_Mitoses)
print ('---------------------------------------------------')
print ('skew_Clump_Thickness = ', 	        skew_Clump_Thickness)
print ('skew_Uniformity_of_Cell_Size = ', 	skew_Uniformity_of_Cell_Size)
print ('skew_Uniformity_of_Cell_Shape = ',      skew_Uniformity_of_Cell_Shape)
print ('skew_Marginal_Adhesion = ', 		skew_Marginal_Adhesion)
print ('skew_Single_Epithelial_Cell_Size = ',   skew_Single_Epithelial_Cell_Size)
print ('skew_Bare_Nuclei = ', 			skew_Bare_Nuclei)
print ('skew_Bland_Chromatin = ', 		skew_Bland_Chromatin)
print ('skew_Normal_Nucleoli = ', 		skew_Normal_Nucleoli)
print ('skew_Mitoses = ', 			skew_Mitoses)
print ('---------------------------------------------------')
print ('TASK 2')
print ('---------------------------------------------------')
print ('pearsonr_prognosis_vs_Clump_Thickness = ', 	        pearsonr_prognosis_vs_Clump_Thickness[0])
print ('pearsonr_prognosis_vs_Uniformity_of_Cell_Size = ', 	pearsonr_prognosis_vs_Uniformity_of_Cell_Size[0])
print ('pearsonr_prognosis_vs_Uniformity_of_Cell_Shape = ',     pearsonr_prognosis_vs_Uniformity_of_Cell_Shape[0])
print ('pearsonr_prognosis_vs_Marginal_Adhesion = ', 		pearsonr_prognosis_vs_Marginal_Adhesion[0])
print ('pearsonr_prognosis_vs_Single_Epithelial_Cell_Size = ',  pearsonr_prognosis_vs_Single_Epithelial_Cell_Size[0])
print ('pearsonr_prognosis_vs_Bare_Nuclei = ', 			pearsonr_prognosis_vs_Bare_Nuclei[0])
print ('pearsonr_prognosis_vs_Bland_Chromatin = ', 		pearsonr_prognosis_vs_Bland_Chromatin[0])
print ('pearsonr_prognosis_vs_Normal_Nucleoli = ', 		pearsonr_prognosis_vs_Normal_Nucleoli[0])
print ('pearsonr_prognosis_vs_Mitoses = ', 			pearsonr_prognosis_vs_Mitoses[0])
print ('---------------------------------------------------')
print ('TASK 3')
print ('---------------------------------------------------')
print ('Please see plots')
plot.figure('Histogram of Clump Thickness for BENIGN prognosis')
plot.hist(bin_benign,color='green')
plot.title('Histogram of Clump Thickness for patients with BENIGN prognosis')
plot.xlabel('Clump Thickness Range 1-10')
plot.ylabel('Number of Patients')

plot.figure('Histogram of Clump Thickness for MALIGNANT prognosis')
plot.hist(bin_malignant,color='red')
plot.title('Histogram of Clump Thickness for patients with MALIGNANT prognosis')
plot.xlabel('Clump Thickness Range 1-10')
plot.ylabel('Number of Patients')
plot.show()

