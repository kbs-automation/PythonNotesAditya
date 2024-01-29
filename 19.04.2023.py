# This is my self python Learning using Online plateform
# simple try to print 
print("hello world")
# add some value
print(20+52)
# print true and false
print (10>5)
print(10<5)
# variable 
name= ("aditya")
print(name)
about_us=("my name is aditya")
print(about_us)
print(type(about_us))
number= (89)
print(number)
print(type(number))
# we can print all variable at same time

print(about_us,number,name)
# to check value
print(id(name),id (number))
c="hello"
print(c,c,c,c,c)


## string concatination

a="aditya"
b="kumar"
print(a+ " + " +b)
two=25
three=30
print(two+three)
print(a+ " " +about_us+ " "+name)

num=30
print(num+50)
print(num+700)
print(num,a)


## (operator in python) Arithemetic operation in python

print (8+2) # it is plush
print (8-2) # it is substract
print (8*2) # it is multiply
print (8/2) # it is divided
print (8**2) ##(**= exponent means power 8*8=64)
print (8//2)  ## floor division
print (8//3) #it will not show the decimal values
print (8%2) #it show the reminder value here 8 is divided by 2 remaing reminder is 0 (%= modulus)
print (8%3) # here 8 is devided by 3 remaing reminder is 2


### Assigment Operators 

# for incraement operators = , exp x=5 , same as x=5
# opr +=, exp x+=3, same as x=x+3
# opr -=, exp x-=3, exp x=x-3

x=5
print (x)
x=x+1  #increament of 1
print(x)
x+=5 #increament of 5
print(x)

# decreament number
x=x-1
print(x)
x-=5
print(x)

a=10
a=a*2
print(a)
a=a/2
print(a)

## Comparsion Operators in Python

 #  Operator        Name           Example
 #  ==              Equal          x==y
 #  !=           Not Equal         x!=y
 #  >            Greator than      x>y
 #  <            Less than         x<y
 #  >=     Greator than or equal   x>=y
 #  <=     Less than or equal      X<=y


l=10
m=20
print(l==m)
print(l!=m)
print(l>m)
print(l<m)
print(l>=m)
print(l<=m)

## Logical Operators in Python

#   Operators           Description                                                  Exmaple
#   and             Returns Ture if both satements are ture                          x<5 and x<10
#   or              Returns Truen if one statements is true                          x<5 or 4<4
#   not             Reverse the result, return false if the result is ture           not(x<5 and x<10)
# not is opposite of true if true come not will change it in false, and false will change in ture


j=10
k=20
print(j==10 and k>j and k!=j and j==10)
print(j>k and J<k)
print(j>k or k==20 or j==k)
print(not j<k)
 

## Membership operators in python
#   Operators                                     Description                                                    Example
#       in          Return True if a sequence with the specified value is present in the object                   x in y
#    not in         Return True if a sequence with the number specified value is not present in the object        x not in y

ar="hello"
print('e' in ar)
print('H' not in ar)
l=[10,20,30,40]
print(60 in l)
print(30 in l)
print(100 not in l)


## Identity Operators in Python
#   Operators                                     Description                                                    Example
#    is                             Return True if both variables are the same object                     x is y
#   is not                          Return True if both varibles are not the same object                  x is not y

xy=10
xz=10
print(xy is xz)
print(xy is not xz)
print(xy==xz)
print(xy!=xz)

## Bitiwise Operators in Python

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

nb=10
bn=8
print(bin(nb))  # print for binary number of 10
print(bin(bn))  # print for binary number of 8
print(bin(nb&bn),nb&bn)
print(bin(nb|bn),nb|bn)
print(bin(nb^bn),nb^bn)




#############################################################


#    DATA Type in Python
# * Mutable object can change its state or contents and immutable object cannot

# Mutable data types:
# list, dictionary, byte array

# Immutable data types 
# int, float, complex, string, tuple, set

# number
a=5
print(a,type(a)) # int
a=5.5
print(a,type(a)) # float
a=2+6j
print(a,type(a)) # complex

## String
# A string is a collection of one or more characters put in a single quote, double quote or triple quote
# Multi line string can be denoted using triple quotes , '''or """

s='hello this is single quotions line '
print(s,type(s))

b="hello this is double quotion line"
print(b,type(b))

c='''this is three qutotion lline
we can write according to want
here many time i enter , but it will print same
thanks and regards aditya
'''
print(c,type(c))
c="""this is three qutotion lline
we can write according to want
here many time i enter , but it will print same
thanks and regards aditya
"""
print(c,type(c))


## List
# List is an ordered sequence of items, it is one of the most used datatype in python and is very flexible. it is using by []. square bracket

l=[10,20,88,5.5]
l[2]=99            # update data
l[3]=5.8           # update data
print(l,type(l))


# tuple

# Tupke is an ordered sequence of items same as a list, it is defined within parentheses () where items are separated by commas.

t=("hello",10,20.5,'tp',5j)
print(t,type(t))


# Dictionary

# Dictionary is an unordered collection of key-value pairs, in python, dictionary are defined within braces {} 
# with each item being a pair in the form key:value

d={ "god":"ram",
   "mom":"maa",
   "num":89,
   88:"nuu"
 
}
print(d["mom"])
print(d,type(d))


#