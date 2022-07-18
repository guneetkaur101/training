
rows = int(input('Enter the number of rows::'))
for i in range(0,rows):
    for j in range(0,i+1):
        print(i+1, end=' ')
    print('')

 # **********Right triangle pyramid of Stars****************

rows=int(input("Enter the number of rows::"))
for j in range(1, rows+1):
   print("* " * j)


# ***********pyramid pattern of asterisk***************
for x in range(0,rows):
    for y in range(0,x+1):
        print("* " ,end=" ")
    print("\r")     

# ************Number triangle pattern******************
rows = int(input('Enter the number of rows::'))
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")
# ************Multiplication table pattern*******************
rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()
