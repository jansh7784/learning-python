
'''str1="ansh jain is a hero "
for i in range(-12,-1):
    print(str1[i])
    

n=int(input("enter any number:"))
for i in range(n,0,-1):
    print(" ")
    for j in range(1,i):
        print(j,end="")'''
'''       
     
a=int(input("enter any value"))
while a<20:
    if a==10:
        continue
    print(a)
    a+=1
    '''
'''    
#wap to input and print table   
n=int(input("enter any number:-"))
for i in range(1,12):
    print("%i * %i = %i" %(n,i,n*i))


n=int(input("enter any number:-"))
for i in range(0,11):
    print("%i * %i = %i" % (n,i,n*i))




    
#fizz buzz problem
a=int(input("enter start"))
b=int(input("enter end"))
for i in range(a,b):
    if i%5==0 and i%3==0:
        print("fizz buzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)

'''



#write a program to print and input number again againuntill user enters nothing 
    

  
while(True):
    a=input("enter number:")
    if(a==""):
        break


while(True):
    a=str(input("enter no."))
    if not a:
        break
      
    
      


