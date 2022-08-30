first = int(input("Please input first number : "))
second = int(input("Please input second number : "))
if first < second :
  min = first
else :
  min = second
#print("Check min number" ,min)

for i in range(min,2,-1) :
  if first%i == 0 and second%i == 0 :
    result = i
    break
print("The greatest common divisor is ", result)
