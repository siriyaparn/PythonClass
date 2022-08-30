letter = input("Please input a letter that you want to check a palindrome : ") 
if(letter == letter[::-1]):  
    print("The letter", letter,"is a palindrome.")  
else:  
    print("The letter", letter,"is not a palindrome.") 