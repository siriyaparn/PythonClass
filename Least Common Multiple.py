first = int(input("Please input first number : "))
second = int(input("Please input second number : "))
if first < second :
  min = first
else :
  min = second
#print("Check min number" ,min)

for i in range(min, 0,-1) :
  if first%i == 0 and second%i == 0 :
    result = i
    fraction1 = first/result
    fraction2 = second/result
    break
print("The least common multiple is ", result*fraction1*fraction2)