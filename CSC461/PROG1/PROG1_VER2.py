
'''
Program Name:  	Pattern Recognition in Python
Instructor:		Dr. Weiss
Class:			CSC461-Programming languages
Author:   	 	Forrest Miller and Yanlin Li
Due Date:      	Sep 24th, 2015
note:           The result for Iris database is not 
				perfectly match, However, it is very
				close to the result in the example.
				I also added extra space in the output file.
Todo:			None	
'''
'''
list of library needed for the program 
'''
import sys
import csv
import math
import copy

'''
This function takes in a 2d list as input, and return a 
list as output. each each elements in the returned list will be 
the minimum item of the column.
'''
def min_vals(data):
    #find max val for each training set
    #initialize the lstt to store minimum values
    min_lst = []
    #go though each feature to find min values
    for i in range(0, len(data[1])):
        #define datatype
        datatype = float
        #find the minimum value of each row  
        lst_of_lst = (datatype(row[i]) for row in data)
        least_val = min(lst_of_lst)
        #append the minimum value of the lstt of minimum values
        min_lst.append(least_val)
    #return the lstt of minimal values lstt
    return min_lst  

'''
This function takes in a 2d list as input, and return a 
list as output. each each elements in the returned list will be 
the maximum item of the column.
'''
def max_vals(data):
    #find max value for each training set
    #initialize the lstt to store max values
    max_lst = []
    #go though each feature to find min values
    for i in range(0, len(data[1])):
        datatype = float
        #find max for each colums
        lst_of_lst = (datatype(row[i]) for row in data)
        max_val = max(lst_of_lst)
        max_lst.append(max_val)
    #return the max values lstt
    return max_lst 

'''
This function will take in a list of 2d lists, and another 2
lists as input, return another 2d lists.
This function will normalize each elements of lists so that
each elements will be in the range between [0,1]
'''
def normalize(data, min_vals, max_vals):
    #This function normalize the data
    #loop though the lstt, normalize each index
    #print (data)
    #print(len(data))
    temp_lst = []
    for i in range(0, len(data)):
        sub_lst = [int(data[i][0])]
        #initialize another lstt to store data for each row
        for j in range(1, len(data[i])):
        	#normallize the data set
            sub_lst.append((float(data[i][j]) - min_vals[j])/\
            	(max_vals[j] - min_vals[j]))
        temp_lst.append(sub_lst)
    #return normalized data
    #print(len(temp_lst))
    return temp_lst

'''
This function will take a 2d list as input, return a list.
This function will calculate the centroid of each data set.
'''
def centroid(data):
	#classifiy determines which class the sample beloing to
    classify = int
    #count total number of elements for each class
    counter = [0]
    #list that stores centroids
    centroid_lst = [[0]* (len(data[0])-1)]
    #this loop add all the data sample tegether
    for i in range(0, len(data)):
       classify = data[i][0]
       #omit the first index since it is the class
       temp = data[i][1:]
       #insert a new element if classify is increased
       if classify+1 > len(centroid_lst):
           counter.insert(classify, 1)
           centroid_lst.insert(classify, [0]* (len(data[0])-1))
       else:
       	   #add each data sample together
           counter[classify] = counter[classify]+1
           centroid_lst[classify] = [ x + y for \
           x, y in zip(centroid_lst[classify], temp)]
    #devide total by numbers of elements
    for i in range(0, len(centroid_lst)):
           centroid_lst[i] = [ x/counter[i] for x in centroid_lst[i]]
    return centroid_lst

'''
This function will take a list and a 2d lists,
return a integer.
This function will return the index of centroid that has the 
minimal distant.
'''
def min_dis(tst_smp, centroid_lst):
    #set min val to a large value
    min_val = 100000000;
    #set min index to -1
    min_index = -1
    for i in range(0, len(centroid_lst)):
    	#calculate the minimal distance 
        temp = math.sqrt(sum([(float(x)-y)**2 for \
        	x,y in zip( tst_smp, centroid_lst[i])]))
        #set min val to temp if temp is less than min val
        if temp < min_val:
            min_val = temp
            min_index = i
    return min_index
        

'''
The following code are for the main function
'''
'''
Variables needed for the program
'''

#print out consists 3 column id, pridict class, actual class

print_out = []
#numbers of each classes
counter = [0]
#number of incorrect classification
num_incrt = [0]

'''
I copied the following 4 lines of code from Dr.Weiss's web page
'''
# get filename as command-line argument
filename = sys.argv[1]

'''
check if file is open
'''
# open CSV file (automatically closed at end of with stmt)
try:
    with open( filename ) as fin:
    	# read the file with the csv reader
        reader = csv.reader( fin )  
        # convert the csv reader object (a generator) to a list (of lists)
        data = list( reader )    
except IOError:
    print ("Could not open file! Please check if the file name is corret!")
    exit()

#save a copy for a original data
orginal = copy.deepcopy(data)

#remove first 2 rows and first column
header = data[0]
del data[0]
del data[0]

#sort data based on its class
data = sorted(data, key = lambda x:x[1])

#save id into id list, and remove id from the list
for i in data: 
    print_out.append([int(i[0])])
    i.pop(0)

#normalise whole data set
nor_data = normalize(data, min_vals(data), max_vals(data))

#find pridict class for each elements
for i in range(0, len(nor_data)):
    tst_smp = nor_data[i]
    temp = tst_smp[1:]
    #delete the test sample
    del nor_data[i]
    #find centroid for each class
    centroid_lst = centroid(nor_data)
    min_idx = min_dis(temp, centroid_lst)
    #add test samples into the print out list
    print_out[i].append (tst_smp[0])
    print_out[i].append (min_idx)
    #insert the test sample back to nor_data
    nor_data.insert(i, tst_smp)



#This loop counts the numbers of elements in each classes
#THis loop also counts incorrect number of each classes
for i in range(0, len(print_out)):
    #save classify into a variable 
    classify = print_out[i][1]
    if classify+1 > len(counter):
        counter.append(1)
        num_incrt.append(0)
    else:
        counter[classify] = counter[classify] + 1
    if print_out[i][1] != print_out[i][2]:
    	#count the number of incorrect calssification
        num_incrt[classify] = num_incrt[classify] + 1



#print results to the screen
print(header[0])
for i in range(0, len(counter)):
	#calculae percentage
    temp = 100*((counter[i]-num_incrt[i])/counter[i])
    print('class ', i, '(', header[i+1][2:],'): ', counter[i],' samples, ', 
        "%.1f"%temp, '% accuracy') 

#sort the list based on its id,
print_out = sorted (print_out, key = lambda x:x[0])

#get the file name
o_file = filename.split('.')[0]
o_file = o_file + '.cv'

'''
This blocks of code opens file, and write information into it.
'''
try:
    sys.stdout = open(o_file, 'w')
    print (header[0])
    for i in range(0, len(counter)):
        temp = 100*((counter[i]-num_incrt[i])/counter[i])
        print('class ', i, '(', header[i+1][2:],'): ', counter[i],' samples, ',
            "%.1f"%temp, '% accuracy') 
    print('\n')
    print ('Sample, ', 'Class, ', 'Pridicted')
    for i in range(0, len(print_out)):
        if print_out[i][1] != print_out[i][2] :
            print(print_out[i][0],", ",  print_out[i][1], 
            	", ", print_out[i][2], "*")
        else:
            print(print_out[i][0],", ",  print_out[i][1],", ", print_out[i][2])
    sys.stdout.close()
except IOError:
    print ("Could not open file! Please check if the file name is corret!")
    exit()
#print(print_out)

#print (filename)
#print (header)
#print(len(pridict_lst), "", prdict_lst,"\n", act_lst, "\n")
