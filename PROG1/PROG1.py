import sys
import csv
import math

def min_vals(data):
    #find max val for each training set
    #initialize the list to store minimum values
    min_lis = []
    #go though each feature to find min values
    for i in range(1, len(data[1])):
        #define datatype
        datatype = float
        #find the minimum value of each row  
        lis_of_lis = (datatype(row[i]) for row in data)
        least_val = min(lis_of_lis)
        #append the minimum value of the list of minimum values
        min_lis.append(least_val)
    #return the list of minimal values list
    return min_lis  

def max_vals(data):
    #find max value for each training set
    #initialize the list to store max values
    max_lis = []
    #go though each feature to find min values
    for i in range(1, len(data[1])):
        datatype = float
        lis_of_lis = (datatype(row[i]) for row in data)
        max_val = max(lis_of_lis)
        max_lis.append(max_val)
    #return the max values list
    return max_lis 



def normalize(data, min_vals, max_vals):
    #normalize the function
    #initialize a new list to store normalized data
    temp_lis = []
    #loop though the list, normalize each index
    for i in range(0, len(data)):
        #initialize another list to store data for each row
        temp_sub_lis = [int(data[i][0])]
        for j in range(0, len(min_vals)):
            temp = (float(data[i][j+1]) - min_vals[j])/(max_vals[j] - min_vals[j])
            temp_sub_lis.append(temp)
        #append the sub list to the lists
        temp_lis.append(temp_sub_lis)
    #return normalized data
    return temp_lis

def centroid(data):
    centroid_lis = []
    counter = []
    classify = int
    #total = [0]*len(data[0])
    for i in range(0, len(data)):
        classify = data[i][0]
        temp = data[i][1:]
        if classify+1 > len(centroid_lis):
            centroid_lis.append(temp)
            counter.append(1)
        else:
            counter[classify] = counter[classify] + 1
            centroid_lis[classify] = [x + y for x, y in zip(centroid_lis[classify], temp)]
    #print (counter, len(counter))
    for i in range(0, len(centroid_lis)):
        for j in range(0, len(centroid_lis[i])):
            centroid_lis[i][j] = centroid_lis[i][j] / counter[i]
    #print (centroid_lis) 
    return centroid_lis



def min_dis(tst_smp, centroid_lis):
	#set min val to a large value
    min_val = 100000000;
    #set min index to -1
    min_index = -1
    for i in range(0, len(centroid_lis)):
        temp = math.sqrt(sum([(float(x)-y)*(float(x)-y) for x,y in zip( tst_smp, centroid_lis[i])]))
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
    data = list( reader )    # convert the csv reader object (a generator) to a list (of lists)
#save a copy for a original data
orginal = data
#remove first 2 rows and first column
del data[0]
del data[0]
for i in data: i.pop(0)

# print out contents, one line at a time
#for i in data: print(i)

min_idx_lst = []
for i in range(0, len(data)):
    temp = data[i]
    del data[i]
    min_lis = min_vals(data) 
    max_lis = max_vals(data)
    nor_data = normalize(data, min_lis, max_lis)
    centroid_lis = centroid(nor_data)
    min_idx_lst.append(min_dis(temp, centroid_lis))
    data.insert( i, temp)


for i in range(0, len(min_idx_lst)): print(min_idx_lst[i])


'''
# alternatively: could read in one line at a time
fin = open( filename )
for row in csv.reader( fin ): print( row )
fin.close()     # no with_as block, so must close file manually
'''