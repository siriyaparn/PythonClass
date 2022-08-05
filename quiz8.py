import numpy as np

m = int(input("What size of the matrix do you wamt : ")) # assign size of matrix
n = m   # to make a square matrix
a = []  # assign list

for i in range (1,m+1): #create for loop for i = 1,2,3
    for j in range (1,n+1): #create for loop for j = 1,2,3
        if i < j and j != m: 
            a.append(0) # append 0 to list a if i < j and j != m
            #print(i)
            #print(j)
            #print(m)
            #print(a)
        elif i == j or j == m:
            a.append(1) # append 1 to list a if i == j or j == m
            #print(i)
            #print(j)
            #print(m)
            #print(a)
        else:
            a.append(-1) # else append -1 to list a 
            #print(i)
            #print(j)
            #print(m)
            #print(a)
            
matrix = np.array([a]).reshape(m,n) #create matrix by using array and reshape array follow m,n dimension
print(matrix) # show the matrix
