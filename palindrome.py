def pal_indrome(string):
    reversed_string = string[::-1]
    status = 1
    if(string != reversed_string):
        status = 0
    return status

string = input("Enter a word: ")
status = pal_indrome(string)
if status:
    print("It is a palindrome!")
else:
    print("No, it is not!")