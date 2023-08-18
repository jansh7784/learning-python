
#WITH USING 3RD VARIABLE

a = int (input ("enter the first number: "))    
b = int (input ("enter the second number: "))
temp=a
a=b
b=temp
print("value of a :",a)
print("value of b:",b)

#WITHOUT USING 3RD VARIABLE

a = int (input ("enter the first number: "))    
b = int (input ("enter the second number: "))

print("BEFORE SWAPPING")
print("value of first no is:",a, "value of second no is:",b)

a , b = b , a

print("AFTER SWAPPING")
print("value of first no is:",a, "value of second no is:",b)
