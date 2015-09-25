import sys
import csv
import math

def split_lst(data):
    new_data = []
    for i in range(0, len(data)):
        classify = int(data[i][0])
        if classify+1 > len(new_data):
            new_data.insert(classify, [])
        new_data[classify].append(data[i][1:])
    #print(new_data)
    return new_data

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

def max_vals(data):
    #find max value for each training set
    #initialize the lstt to store max values
    max_lst = []
    #go though each feature to find min values
    for i in range(0, len(data[1])):
        datatype = float
        lst_of_lst = (datatype(row[i]) for row in data)
        max_val = max(lst_of_lst)
        max_lst.append(max_val)
    #return the max values lstt
    return max_lst 



def normalize(data, min_vals, max_vals):
    #This function normalize the data
    #initialize a new lstt to store normalized data
    temp_lst = []
    #loop though the lstt, normalize each index
    for i in range(0, len(data)):
        temp_sub_lst = []
        #initialize another lstt to store data for each row
        for j in range(0, len(min_vals)):
            temp = (float(data[i][j]) - min_vals[j])/(max_vals[j] - min_vals[j])
            temp_sub_lst.append(temp)
        #append the sub lstt to the lstts
        temp_lst.append(temp_sub_lst)
    #return normalized data
    return temp_lst

def centroid(data):
    centroid_lst = []
    #total = [0]*len(data[0])
    for i in range(0, len(data)):
       centroid_lst = [x + y for x, y in zip(centroid_lst[classify], temp)]
    #print (counter, len(counter))
    for i in range(0, len(centroid_lst)):
        for j in range(0, len(centroid_lst[i])):
            centroid_lst[i][j] = centroid_lst[i][j] / counter[i]
    #print (centroid_lst) 
    #print ('\n')
    return centroid_lst



def min_dis(tst_smp, centroid_lst):
    #set min val to a large value
    min_val = 100000000;
    #set min index to -1
    min_index = -1
    for i in range(0, len(centroid_lst)):
        temp = math.sqrt(sum([(float(x)-y)**2 for x,y in zip( tst_smp, centroid_lst[i])]))
        #set min val to temp if temp is less than min val
        if temp < min_val:
            min_val = temp
            min_index = i
    #print ('\n')
    return min_index


def print_result(tst_smp ):
    print('')

# get filename as command-line argument
filename = sys.argv[1]

# open CSV file (automatically closed at end of with stmt)
with open( filename ) as fin:
    reader = csv.reader( fin )  # read the file with the csv reader
    data = list( reader )    # convert the csv reader object (a generator) to a lstt (of lstts)
#save a copy for a original data


orginal = data
#remove first 2 rows and first column
del data[0]
del data[0]
for i in data: i.pop(0)

#A lstt stores index for each min dis
min_lst_lst = []
max_lst_lst = []
min_idx_lst = []
nor_data_lst = []
centroid_lst = []


new_data =  split_lst(data)
for i in range( 0, len(new_data)):
    min_lst = min_vals(new_data[i])
    max_lst = max_vals(new_data[i])
    min_lst_lst.insert(i, min_lst)
    max_lst_lst.insert(i, max_lst)
    nor_data = normalize(new_data[i], min_lst_lst[i], max_lst_lst[i])
    nor_data_lst.insert(i, nor_data)
    #print (len(nor_data))
    print (nor_data_lst[i], '\n\n\n')
    centroid = centroid( nor_data_lst[i])
    #print (centroid)
    centroid_lst.insert( i, centroid)

for i in range( 0, len(nor_data_lst)):
    for j in range( 0, len(nor_data_lst[i])):
        tst_smp = nor_data_lst[i][j]
        del nor_data_lst[i][j]
        centroid_lst[i] = centroid(nor_data)
        min_idx = min_dis( tst_smp, centroid_lst)
        min_idx_lst.append(min_idx)

print (min_idx_lst)





#print (min_vals(data))
'''
for i in range(0, len(data)):
    tst_smp = data[i]
    del data[i]
    min_lst = min_vals(data) 
    max_lst = max_vals(data)
    nor_data = normalize(data, min_lst, max_lst)
    centroid_lst = centroid(nor_data)
    min_idx_lst.append(min_dis(tst_smp, centroid_lst))
    data.insert( i, tst_smp)


#for i in range(0, len(min_idx_lst)): print(min_idx_lst[i])


def min_vals(data):
    #find max val for each training set
    #initialize the lstt to store minimum values
    min_lst = []
    #go though each feature to find min values
    for i in range(1, len(data[1])):
        #define datatype
        datatype = float
        #find the minimum value of each row  
        lst_of_lst = (datatype(row[i]) for row in data)
        least_val = min(lst_of_lst)
        #append the minimum value of the lstt of minimum values
        min_lst.append(least_val)
    #return the lstt of minimal values lstt
    return min_lst  

def max_vals(data):
    #find max value for each training set
    #initialize the lstt to store max values
    max_lst = []
    #go though each feature to find min values
    for i in range(1, len(data[1])):
        datatype = float
        lst_of_lst = (datatype(row[i]) for row in data)
        max_val = max(lst_of_lst)
        max_lst.append(max_val)
    #return the max values lstt
    return max_lst 

def min_vals(data):
    #find max val for each training set
    #initialize the lstt to store minimum values
    min_lst = [99999.0]*(len(data[0])-1)
    min_lst_lst = []
    #go though each feature to find min values
    for i in range(0, len(data)):
        classify = int(data[i][0])
        #find the minimum value of each row  
        if classify+1 > len(min_lst_lst):
            min_lst_lst.insert(classify, min_lst)
        for j in range(0, len(data[i])-1):
            if float(data[i][j+1]) < (min_lst_lst[classify][j]):
            min_lst_lst[classify][j] = float(data[i][j+1])
    return min_lst_lst

def min_vals(data):
    #find max val for each training set
    #initialize the lstt to store minimum values
    min_lst = [99999.0]*(len(data[0])-1)
    min_lst_lst = []
    #go though each feature to find min values
    for i in range(0, len(data)):
        classify = int(data[i][0])
        #find the minimum value of each row  
        if classify+1 > len(min_lst_lst):
            min_lst_lst.insert(classify, min_lst)
        for j in range(0, len(data[i])-1):
            if float(data[i][j+1]) < (min_lst_lst[classify][j]):
                min_lst_lst[classify][j] = float(data[i][j+1])
    return min_lst_lst
'''