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
    print("It is a palindrome ")
else:
    print("Sorry! Try again")

#     number=int(input("Enter any number :"))

# temp=number
# reverse_num=0
# while(number>0):
#     digit=number%10
#     reverse_num=reverse_num*10+digit
#     number=number//10
# if(temp==reverse_num):
#     print("The number is palindrome!")
# # else:
#     print("Not a palindrome!")

    # list is changeable append
    # different Variable
    
