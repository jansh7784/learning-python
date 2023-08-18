#STRIING REPLACING
str1="Kkkkomalamkkmk"
print(str1.strip("kalm"))


str1="kkkkkmal ankklmka anmma 800"  
print(str1.strip("kalm"))
print(len(str1))          #function fo rfinding number
print(str1.capitalize())  #functions capitalize() first letter captial of first word
print(str1.title())     #functions title() all lettter first word capital
print(str1.isupper())   #all upper letter then true
print(str1.islower())   #all small letter then true
print(str1.count("k",5))    #count letter which you give given 5 so after fifth letter it wil count
print(str1.find("l",8))   #finds vlaue at which number or index
print(str1.index("n",3))   #find the no 1st digit or its index place
print(str1.isalpha())'   #if only alphabet then true else false
print(str1.isdigit())       #if only number then true else false
print(str1.isnumeric())       #same work as above 
print(str1.isspace())    #check space is there and only space then true else false
print(str1.isalnum())    #aplhanumeric value without space true
print(str1.partition("a"))
print(str1.split("a"))
l1=('kkkkkm', 'a', 'l ankklmka', '', 'anmma 800')
print("-".join(l1))  #to jjoin emplty elements in list with what u want
print(str1.endswith("0"))
print(str1.startswith("s"))
print(dir(str1))
print(help(str.upper))











'''  FUNCTIONS OF print(dir(str)) string

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__'
, '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']

'''
