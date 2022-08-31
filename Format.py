
bnum = input("Enter the Binary Number : ")
b1,b2 = bnum.split(".")

b1 = int(b1)
b2 = int(b2)

d1 = 0
d2 = 0
i = 1
j = 1
while b1!=0:
    rem1 = b1%10
    d1 = d1 + (rem1*i)
    print (i)
    b1 = int(b1/10)

while b2!=0:
    rem2 = b2%10
    #print (rem2)
    d2 = d2 + (rem2*j)
    #print (d2)
    j = j**-2
    print (j)
    b2 = int(b2/10)
    #print(b2)

print("Equivalent Decimal Value = ", d1,".",d2)