'''

a="anj" + "ali"
print(a)
a="and" + "vind"
print(a)
a="anj" *4
print(a)
#addition of string




#slicing of string

str1="India is my country"
print(str1[0:5])
print(str1[-1:-6:-1])
print(str1[13:18])


str1=str(input("enter any string:"))
print(str1[:50])
print(str1[::-1])
print(str1[1:50:2])




str1=' INDIA '
str2=str1
print(id(str1))
print(id(str2))
print(str1.upper())  #converts into uppercase
s3=str1.lower()   #converts into smallcase
print(s3)
print(id(s3))
s4=str1.lower()
print(s4)
print(id(s4))
s5=str1.strip()  #remove spaces
print(s5)
s6=str1.rstrip()  #remove spaces fron right
print(s6)
s7=str1.lstrip()  #remove spaces from light

'''

str1=str(input("enter any string:"))
str2="love india is my country "
s2=str1.replace("I" , "T" )   #REPLACE WORDS WITHIN INPUT STRING
print(s2)
s3=str2.strip('i')
print(s3)
s4=str2.split()
print(s4)
s5=str2.split('i',1)  # 1 st element me i wala hatega then pura llist bn jayega 
print(s5)

