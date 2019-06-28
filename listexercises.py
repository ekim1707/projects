# 1. Sum the Numbers
# Given an list of numbers, print their sum. When I say given something, just make something up and store it in a variable.
x = 0
while x == 0:
    firstinput = input('Enter a number: ')
    ifirstinput = int(firstinput)
    numberList = []
    numberList.append(ifirstinput)
    y = 0
    while y == 0:
        endlist = input('Do you want to stop? (Y or N) ')
        if endlist == 'Y' or endlist == 'y':
            x = 1
            break
        elif endlist == 'N' or endlist == 'n':
            y = 1
        else:
            print('Invalid response!')

totalsum = 0
for x in numberList:
    totalsum += x
print(totalsum)

# 2. Largest Number
# Given an list of numbers, print the largest of the numbers.
# 
# 3. Smallest Number
# Given an list of numbers, print the smallest of the numbers.
# 
# 4. Even Numbers
# Given an list of numbers, print each number in the list that is even.
# 
# 5. Positive Numbers
# Given an list of numbers, print each number in the list that is greater than zero.
# 
# 6. Positive Numbers II
# Given an list of numbers, create a new list which contains every number in the given list which is positive.
# 
# 7. Multiply a list
# Given an list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in
# the first list multiplied by the factor. Print this list.
# 
# 8. Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding
# positions in the two lists. Example:
# 
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# 9. Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
# 
# [ [2, -2], [5, 3] ]
# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum 
# of the numbers in the corresponding addend matrices. Example: to add
# 
# 1 3 2 4
# and
# 
# 5 2 1 0
# results in
# 
# 6 5 3 4
# 10. Matrix Addition II
# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the
# same size.
# 
# 11. De-dup
# Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any
# duplicate values removed. Print the list.
# 
# Bonus: Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices.
# Print the resulting matrix. How do you multiple two matricies?
# https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-intro