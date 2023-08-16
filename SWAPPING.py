#swap using 3rd variable

a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))
temp=a   #temp=a
a=b      #a=b
b=temp  #b=a

print("value of a :",a)
print("value of b:",b)

#hence values are swapped


#swap without using 3rd variable

a = int(input("Enter the first variable: "))
b = int(input("Enter the second variable: "))

print("BEFORE SWAPPING:")
print("value of a:",a , "value of b:",b )

a ,b = b ,a  #THIES OPERATION CHANGES VLAUE OF A ND B

print("AFTER SWAPPING:")
print("value of a:",a , "value of b:",b )

#hence values are swapped


'''
Enter the first variable: 8
Enter the second variable: 2
value of a : 2
value of b: 8
Enter the first variable: 8
Enter the second variable: 2
BEFORE SWAPPING:
value of a: 8 value of b: 2
AFTER SWAPPING:
value of a: 2 value of b: 8
'''