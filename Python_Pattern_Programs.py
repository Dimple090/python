# # # #To print given number of *s in a row
# # # n=int(input("Enter the value of n :"))
# # # for i in range(n):
# # #     print('*',end =' ')
# # # #note:-This will print n asterisks on the same line, separated by spaces. For example, if n is 5, the output will be:* * * * *
# # # n=int(input("Enter the value of n :"))
# # # for i in range(n):
# # #     print('*')
# # # #note:-This will print n asterisks, each on a new line. For example, if n is 5, the output will be:
# # # # *
# # # # *
# # # # *



# # #To print square pattern with * symbols
# # n=int(input('Enter the number of rows:'))
# # for i in range(n):
# #     print('* '*n)



# # #To print square pattern with provided fixed digit
# # n=int(input("Enter the number of rows:"))
# # for i in range (n):
# #     print((str(n)+' ')*n)



# # #To print square pattern with provided fixed digit in every row
# # n=int(input("Enter the number of rows:"))
# # for i in range(n):
# #     print((str(i+1)+' ')*n)



# # # To print square pattern with fixed alphabet symbol
# # n=int(input('Enter the row:'))
# # for i in range(n):
# #     print('A '*n)




# # ##To print square pattern with provided fixed alphabet in every row
# # n=int(input("Enter the number of rows:"))
# # for i in range(n):
# #     print((chr(65+i)+' ')*n)




# # #To print right angle triangle pattern with fixed alphabet symbols in every 
# # n=int(input('Enter no of rows:'))
# # for i in range(n):
# #     print((chr(65+i)+' ')*(i+1))#65 means A,66 means B , 67 means C and so on




# #To print inverted right angle triangle pattern with *symbols
# n=int(input("Enter no of rows:"))
# for i in range(n):
#     print('* '*(n-i))


# #invereted right angle triangle pattern with digits in ascending in every row
# n=int(input("Enter no of rows:"))
# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end=' ')
#     print()



# #To print pyramid pattern with fixed digit in every row
# n=int(input("Enter the no of rows:"))
# for i in range(n):
#     print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))#n-i-1:no of spaces in every row ; i+1: which symbol ; i+1:how many times





# #pyramid pattern with alphabet symbols in reverse of dictionary order in every row
# n=int(input("Enter no of rows:"))
# for i in range(n):#0,1,2,3
#     print(' '*(n-i-1),end=' ')#no of spaces in every row=n-i-1
#     for j in range(i+1):#no of symbols in each row: i+1
#         print(chr(64+n-j),end=' ')#which symbols we have to generate
#     print()






# #right half diamond pattern with alphabet symbols in dictionary order in every row
# n=int(input("Enter n values:"))
# for i in range(n):
#     for j in range(i+1):#how many symbols:i+1
#         print(chr(65+j),end=' ')#which symbol:65+j
#     print()
# for i in range (n-1):#no of rows
#     for j in range(n-i-1):#no of symbols in each every row
#         print(chr(65+j),end=' ')#which symbol:65+j
#     print()







# # inverted pyramid pattern with alphabet symbols in dictionary order in every row
# n=int(input("Enter no of rows:"))
# for i in range (n):
#     print(' '*i,end=' ')#no of spaces in every row:i
#     for j in range(n-i):#no of symbols in every row:n-i
#         print(chr(65+j),end=' ')
#     print()








# #to print diamond pattern with *symbols
# n=int(input("Enter no of vaalue:"))
# for i in range(n):
#     print(' '*(n-i-1)+'* '*(i+1))#no of spaces in each row:n-i-1;no of *'s in each row:i+1

# for i in range(n-1):#no of rows
#     print(' '*(i+1)+'* '*(n-i-1))#no of spaces in each row:i+1;no of *'s in each row:n-i-1
# print()






# #to print right half diamond pattern with *symbols
# n=int(input("Enter a number:"))
# for i in range(n):
#     print('* '*(i+1))
# for i in range(n-1):
#     print('* '*(n-i-1))
# print()
     





# #to print left half diamond pattern with *symbols
# n=int(input("Enter a value:"))
# for i in range(n):
#     print('  '*(n-i-1)+'* '*(i+1))
# for i in range(n-1):
#     print('  '*(i+1)+'* '*(n-i-1))







# #To print top hallow diamond pattern with *symbols
# n=int(input("Enter no of rows:"))
# for i in range(n):
#      print('  '*(n-i-1)+'* ',end='')#no of spaces before star*:n-i-1
#      if i>=1:
#           print('  '*(2*i-1)+'*',end='')#no of spaces between 2 *'s:2i-1
#      print()
#explanation above code:Input:
# n: This variable takes the number of rows for the upper half of the diamond from user input.
# Outer Loop (for i in range(n)):
# This loop iterates through each row of the upper half of the diamond. The variable i represents the current row index (starting from 0).
# Leading Spaces:
# print(' ' * (n - i - 1) + '* ', end=''):
# n - i - 1: This calculates the number of leading spaces needed to center the diamond. As i increases, the number of leading spaces decreases.
# This prints the first asterisk (*) in each row.
# Spaces Between Asterisks:
# The if i >= 1 condition checks if the current row is greater than or equal to 1. This is because the first row (when i = 0) should only have one asterisk.
# print(' ' * (2 * i - 1) + '*', end=''):
# 2 * i - 1: This calculates the number of spaces between the two asterisks for the current row (starting from the second row). The pattern increases the space between the asterisks as you move down the rows.
# Moving to the Next Line:
# print(): This function moves the cursor to the next line after printing the asterisks.





# #To print bottom half hallow diamond pattern with *symbols
# n=int(input("Enter no of rows:"))
# for i in range(n):
#     print('  '*i+'* ',end='')#no of spaces before first* symbol:i;
#     if i!=(n-1):#except last row
#         print('  '*(2*n-2*i-3)+'*',end='')
#     print()



 


# #To print full hallow diamond pattern with *symbols
# n = int(input("Enter no of rows: "))
# # Upper half of the diamond
# for i in range(n):
#     print('  ' * (n - i - 1) + '* ', end='')  # Leading spaces and the first '*'
#     if i >= 1:
#         print('  ' * (2 * i - 1) + '*', end='')  # Spaces between two '*'s for rows >= 1
#     print()  # Move to the next line
# # Lower half of the diamond
# for i in range(n):
#     print('  ' * i + '* ', end='')  # Leading spaces for the lower half
#     if i != (n - 1):  # For all rows except the last one
#         print('  ' * (2 * n - 2 * i - 3) + '*', end='')  # Spaces between the '*'s
#     print()  # Move to the next line











 
# # Bottom half diamond pattern with alphabet symbols in reverse of dictionary order
# n = int(input("Enter the number of values: "))

# # Loop to print the bottom half of the diamond
# for i in range(n):
#     # Print leading spaces
#     print('  ' * i, end='')
    
#     # Print the left character
#     print(chr(65 + i), end=' ')
    
#     # Print the middle spaces and right character if not on the last row
#     if i != n - 1:
#         print('  ' * (2 * (n - i - 1) - 1), end='')
#         print(chr(65 + i), end=' ')
    
#     print()  # Move to the next line














#left half diamond pattern with digits in ascending order in every row
# Left half diamond pattern with digits in ascending order
n = int(input("Enter number of n value: "))  # Get the number of rows from the user

# Top half of the diamond
for i in range(n):
    print('  ' * (n - i - 1), end='')  # Print leading spaces
    for j in range(i + 1):
        print(j + 1, end='  ')  # Print digits in ascending order
    # print()  # Move to the next line
    print()
# Bottom half of the diamond
for i in range(n - 1):
    print('  ' * (i + 1), end='')  # Print leading spaces
    for j in range(n - i - 1):
        print(j + 1, end=' ')  # Print digits in ascending order
    print()  # Move to the next line

