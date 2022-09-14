import numpy as np

m = int(input("What size of the matrix do you want : ")) # assign size of matrix
n = m   # to make a square matrix
a = []  # assign list
value = 1

for i in range (1,m+1): #create for loop for i = 1,2,3 and so on
    for j in range (1,n+1): #create for loop for j = 1,2,3 and so on           
        #print("i = " ,i)
        #print("j = ", j)
        #print("j - i = ", j-i)
        value = 2**abs((j-i))
        a.append(value) # append value 
      
matrix = np.array([a]).reshape(m,n) #create matrix by using array and reshape array follow m,n dimension
print(matrix) # show the matrix
