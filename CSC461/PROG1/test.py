import math
a = [[3,2,3],[1,2,3],[4,2,6]]
a= sorted(a, key = lambda x:x[0] )

d = 'file.txt'

print (d.split('.')[0])

b = math.sqrt(sum([(x-y)**2 for x,y in zip( a[0], a[2])]))

c = [0]*3
#print (type(a))
#print (a)