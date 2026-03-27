#indentation is one tab

#for(initialization; condition; increment/decrement)
for i in range(5):  #i =4
    print(i)  #0,1,2,3,4

for i in range(1,11,2):  #i =4
    print(i)  #1,3,5,7,9

for i in range(1,11):  #i =4
    print(i*2)  #2,4,6,8,10,12,14,16,18,20

for i in range(1,11):  
    print(i*2," ",i*3," ",i*4)  

for i in range(1,20):  #i =4
    print("i*--")  



#WAP to print even and odd numbers
for i in range(1,11):  #i =1
    if i%2==0:
        print("Even= ",i)
    else:
        print("Odd= ",i)

#WAP to print the count of even and odd numbers
even=0 #2
odd=0  #1
for i in range(1,11):  #i =5
    if i%2==0:
        even+= 1  #even=2+1=3
    else:
        odd+= 1   #odd=1+1=2
print("Even = ",even)
print("Odd = ",odd)


username = input("Enter username:")  #prashant
password = input("Enter password:")  #prashant
if username==password:
    print("Login successful")
else:
    print("Login failed")




brand=input("Enter your cooldrink name either in upper case or in lower case but not in combine:")
if brand=="pepsi" or brand=="PEPSI":
    print("Swag")
elif brand=="dew" or brand=="DEW":
    print("dar age jeet hai")
elif brand=="thumbsup" or brand=="THUMBSUP":
    print("taste the thunder")
else:
    print("go with your brand")


n1=int(input("Enter First Number"))
n2=int(input("Enter Second Number"))
n3=int(input("Enter Third Number"))
if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else:
    print("Biggest Number is:",n3)


                           #join function
s ="prashant","ashish","sandip"
m ='|'.join(s)
print(m) #prashant|ashish|sandip





                            #find function
s="help4code is a best platform for practicing programming" 
print(s.find("help4code")) 
print(s.find("python"))
print(s.find("programming")) 
#find function return the starting index of given string and if string is not present then it returns defualt value -1


