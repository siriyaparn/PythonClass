text = input("Please input a letter that you want to check a palindrome : ") 
letter = text.lower()
#print (letter)
if(letter == letter[::-1]):  
    print("The letter", text,"is a palindrome.")  
else:  
    print("The letter", text,"is not a palindrome.")

    