# Create function AND
def AND (a,b):
  if a == True and b == True :
    return(True)
  else :
    return(False)

# Create function OR
def OR (a,b):
  if a == False and b == False :
    return(False)
  else :
    return(True)

# Create function NOT
def NOT (a,b):
  if a == False :
    return(True)
  elif a == True :
    return(False)
  elif b == False :
    return(True)
  elif b == True :
    return(False)

# Create function NAND
def NAND (a,b):
  if a == True and b == True :
    return(False)
  else :
    return(True)

# Create function XOR
def XOR (a,b):
  if a == True and b == True :
    return(False)
  elif a == False and b == False :
    return(False)
  else :
    return(True)

# Create function NXOR
def NXOR (a,b):
  if a == True and b == True :
    return(True)
  elif a == False and b == False :
    return(True)
  else :
    return(False)

# Create function NOR
def NOR (a,b):
  if a == False and b == False :
    return(True)
  else :
    return(False)

# Input logic to create truth table
x = input("What logic do you want to create truth table? (Example: a AND b, a OR b): ")
x = x.lower()

# Display truth table
print("The Truth Table")
print("----------------------------------------------------------")
print('|{0:^16}|{1:^16}|{2:^16}'.format('a','b', x))
print("----------------------------------------------------------")
for a in [True,False]:
  for b in [True,False]:
    if x == 'a and b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(AND (a,b))))
    elif x == 'a or b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(OR (a,b))))
    elif x == 'not a' or x == 'not b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(NOT (a,b))))
    elif x == 'a nand b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(NAND (a,b))))
    elif x == 'a xor b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(XOR (a,b))))
    elif x == 'a nxor b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(NXOR (a,b))))
    elif x == 'a nor b':
      print('|{0:^16}|{1:^16}|{2:^16}'.format(str(a),str(b),str(NOR (a,b))))   