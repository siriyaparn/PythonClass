word = input("Please input word to create the shortes palindrome : ")       # Assign the word
length = len(word)                                                          # Assign the length of the word to check palindrome
#print("The length is", length)
init = 0                                                                    # First string starts with index 0 
after = length - 1                                                          # Last string is located at lenght - 1
rev_str = ""
palindrome = ""

while (after > init) :
    if(word == word[::-1]):                                                 # Check if the word is a palindrome
        print(word)
        break                                                               # If the word is a palindrome, break
    else :
        if (word[init] == word[after]) and (word[init+1] == word[after-1]) and (word[init+2] == word[after-2]):     # Case abcb : abcba
            after = after - 1  
            rev_str = word[init] + rev_str                                  # Store value of the rev
            init = init + 1        
            #print ("Rev 1" , rev_str)   
            #print ('check1',init)
        else :                                                              # Case hello : hellolleh
            rev_str = word[init] + rev_str                                  # Store value of the rev
            init = init + 1
            #print ("Rev 2" , rev_str)
            #print ('check2',init)
palindrome = word + rev_str                                                 # Create palindrome word
print(palindrome)                                                           # Print a palindrome word