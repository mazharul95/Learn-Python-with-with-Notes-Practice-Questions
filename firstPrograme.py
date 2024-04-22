#basic print in the output file for debugging purposes 

name = "Piyash"
age = 25
price =100.99
age2 = age
print(name,age2, price)

""" Expression Execution """
#------------------------#
# String and numerical value can operate together with (* multiply)
A, B =2,3
Txt= "@"
print(2*Txt*3)

# # String & string can be operate with (+ plus) (also called concatenations)

A, B ="2", 3
Txt= "@"
print((A+Txt)*B)

# # Numeric value can operate with all arithmetic operations
A, B =2,3
C = 4
print(A+B*C)

# Arithmetic expression with Integer and Float will result in float value
A, B = 1,2
C = A/B
print(C)

#Result of division operator with two integers will be float value
A, B =1,2
C = A/B
print(C)

# # Integer division with float and int will give int displayed as float 
A, B =1.5, 3
C = A//B
print(C)

# floor gives closest integer (floor(number)), which is lesser than or equal to the float value
# Result of (A//B)is the same as (A/B)
A, B =12, 5
C = A//B
print(C)

A, B = -12, 5
C = A//B
print(C)

A, B =12, -5
C = A//B
print(C)

#Remainder is negative when denominator is negative 
A,B = -5,2
C = A%B
print(C)

A, B = 5,2
C = A%B
print(C)

A, B = 5, -2
C = A%B
print(C)

#Comment in Python
#print("hello world")----won't be printed

#single line comment

"""this is 
a multiline 
comment"""