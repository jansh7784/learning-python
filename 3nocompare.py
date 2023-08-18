'''#COMPARE 3 NO USING NESTEDIF ELSE 
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b):
    if(a>c):
        print("a is greater i.e.=",a)
    else:
        print("c is greater i.e=",c)
else:
    if(b>c):
        print("b is greater i.e=",b)
    else:
        print("c is greater i.e=",c)'''

#STRIING REPLACING
str1="Kkkkomalamkkmk"
print(str1.strip("kalm"))


str1="kkkkkmalankkmk aanmma"
print(str1.strip("kalm"))
print(len(str1))          #function fo rfinding number
print(str1.capitalize())  #functions capitalize() first letter captial of first word
print(str1.title())     #functions title() all lettter first word capital
print(str1.isupper())   #all upper letter then true
print(str1.islower())   #all small letter then true
print(str1.count("k",5))    #count letter which you give given 5 so after fifth letter it wil count
print(str1.find("l"))
print(str1.index("n",10))
