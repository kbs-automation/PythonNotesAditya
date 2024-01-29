# Date 29 Jan 2024

# quotation = " "

# What is python ?
# Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

# It is used for:
# web development (server-side),
# software development,
# mathematics,
# system scripting.

# Interpreted means it will read the code line by line and excute it if any line code will incorrect it will stop the read the code
# compilar means it will complile whole code if anything is error they will show without solving error it will not show the output anything
# High level programming means 

# Print function
print("Jai Shri Ram")
print("Welcome to ayodhya" , "Jai Shir Ram")
print(20+10)
print("20+10")
print("aditya kuamr")
print(10>5)
print(20<10)
print(5<10)

##################################################################################################

## Variable in python = Variables are containers for storing data values.
x = "aditya"
y = "kumar"
print(x,y)
name = "roshan"
age = 30
number = 8953304996
print("name",name,"age",age,"number",number)

# String concatenation in python

a1 = "Ram"
a2 = "Charan"
print(a1+" "+a2)
print(a1,a2)


###############################################################
xy = 4       # xy is of type int
xy = "Charan" # xy is now of type str
print(xy)
print(type(xy))
print(type(a1))
print(type(age))
B= "shyam"
print(B)
b= "Daam"
print(b)
print(type(b))

####################################################################
# Multi Words Variable Names
# Camel Case = Each word, except the first, starts with a capital letter: myVariableName = "John"
# Pascal Case = Each word starts with a capital letter: MyVariableName = "John"
# Snake Case = Each word is separated by an underscore character: my_variable_name = "John"

##########################################################################################################

# Python Variables - Assign Multiple Values
# Many Values to Multiple Variables
x1, y1, z1 = "Orange", "Banana", "Cherry"
print(x1)
print(y1)
print(z1)
print(x1,y1,z1)
print(x1+" "+y1+" "+z1) #concatenation

# One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
print(x,y,z,x)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
# This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print(fruits)
print(type(fruits))
print(x,z)

##################################################################################################################

# Python - Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


############################################################
# Python Operators
# Operators are used to perform operations on variables and values.
# In the example below, we use the + operator to add together two values:
print(10 + 5)

# Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Python Arithmetic Operators
# Operator      	Name	      Example	
# +	               Addition	       x + y	
# -	               Subtraction	   x - y	
# *	               Multiplication  x * y	
# /	               Division	       x / y	
# %	               Modulus	       x % y	
# **	           Exponentiation  x ** y	
# //	           Floor division  x // y


x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2 (Exponentiation  x ** y	)
print(x/y) #it is division
print(x%y) # ye kaha tak divide kar skta hai 
print(x//y) # it will not show the value after 0.4 it will show only 0
print(10%3) # it will show the reminder of divison only reminder 1 is answer


################################################################################################################


# Assignment Operators
#Assignment operators are used to assign values to variables:
#Operator	Example	        Same As
# =	         x = 5	        x = 5	
# +=	     x += 3	        x = x + 3	
# -=	     x -= 3	        x = x - 3	
# *=	     x *= 3	        x = x * 3	
# /=	     x /= 3	        x = x / 3	
# %=	     x %= 3	        x = x % 3	
# //=	     x //= 3	    x = x // 3	
# **=	     x **= 3	    x = x ** 3	
# &=	     x &= 3	        x = x & 3	
# |=	     x |= 3	        x = x | 3	
# ^=	     x ^= 3	        x = x ^ 3	
# >>=	     x >>= 3	    x = x >> 3	
# <<=	     x <<= 3	    x = x << 3

x= 5
print(x)
x=x+5
print(x)
x=x-7
print(x)
x=x*2
print(x)
x=x/3
print(x)
x=x//2
print(x)

#################################################################################################################
# Python Comparison Operators
# Comparison operators are used to compare two values:

#Operator	Name	                                         Example
# ==	    Equal	                                         x == y	
# !=	    Not equal	                                     x != y	
# >	        Greater than   	                                 x > y	
# <	        Less than	        print(x!=y)                             x < y	
# >=	    Greater than or equal to	                     x >= y	
# <=	    Less than or equal to	                         x <= y

x = 5
y = 3
z = 5
print(x == y)
print(x==z)
print(x!=y)
print(x!=z)
print(x>y)
print(x<y)
print(y<x)
print(x>=z)
print(x>=y)
print(y>=x)
print(y<=x)
 ###############################################################################################################

#  Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	          Description	                                                        Example
# and 	    Returns True if both statements are true	                     x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	                 x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	not      (x < 5 and x < 10)

x=20
y=10
print(x>y and y<x)
print(x>y or y<x)
print(x>25 or x<8)
print(y>5 or 11<y)
print(not x>25)

##################################################################################################################################
# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	                     Description	                                                                Example
# in 	        Returns True if a sequence with the specified value is present in the object	                x in y	
# not in	    Returns True if a sequence with the specified value is not present in the object	            x not in y

name= "aditya"
print('a' in name)  #true
print('a' not in name) #false

l=[10,20,30,40,60]
print(40 in l)
print(50 in l)
print(50 not in l)

######################################################################################################
# Identity Operators
# Identity operators are used to compare the objects,
# not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	                 Description	                                      Example
# is 	              Returns True if both variables are the same object	      x is y	
# is not	          Returns True if both variables are not the same object	  x is not y

x = "aditya"
y = "aditya"
z = "kumar"
print(x is y)
print(x is not y)
print(x is z)
print(x is not z)

# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator	  Name	                       Description	                                                                         Example
# & 	      AND	               Sets each bit to 1 if both bits are 1	                                             x & y	
# |	          OR	               Sets each bit to 1 if one of two bits is 1	                                         x | y	
# ^	          XOR	               Sets each bit to 1 if only one of two bits is 1	                                     x ^ y	
# ~	          NOT	               Inverts all the bits	                                                                 ~x	
# <<          Zero fill left shift  Shift left by pushing zeros in from the right and let the leftmost bits fall off	 x << 2	
# >>	      Signed right shift    Shift right by pushing copies of the leftmost bit in from the left, 
                                     #and let the rightmost bits fall off	                                             x >> 2

#####################################////////////////////////////////////////////////////////////////////////////////

# operator                      Name                            Descriptipon
# &                             AND                                x & y
# |                             OR                                 x | y
# ^                             XOR                                X ^ y

#         1 = TRUE        -------         0 = FALSE

#    A          B           A&B         A|B         A^B
#    0          0            0           0           0
#    0          1            0           1           1
#    1          0            0           1           1
#    1          1            1           1           0

x = 10
y = 8
print(bin(x))
print(bin(y))
print(x&y,bin(x&y))
print(bin(x&y))