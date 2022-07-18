def check_palindrome_1(string):
    reversed_string = string[::-1]
    print(reversed_string)
    status=1
    if(string!=reversed_string):
        status=0
    return status
string = input("Enter the string: ")
status= check_palindrome_1(string)
if(status):
    print("It is a palindrome string ")
else:
    print("It is not a palindrome string ")