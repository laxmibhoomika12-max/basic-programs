for i in range(1,5):
  if i==3:
       break
print(i)

for i in range(1,5):
   if i==3:
       continue
print(i)

list=[10,20,30,40,50]      #by defualt it take index value 0
for i in list:             #'in' is used to check whether the element is present in the list or not AND it is also called as as membership operator
   print(i)

mycart=[10,20,200,300,800,60,700]
for i in mycart:
   if i>400:
       print("This my purchased cart item")
       continue
   print(i)

#WAP to calculate the sum of the list elements
list=[1,2,3,4,5,6,7,8,9,10]      #by defualt it take index value 0
sum=0
for x in list:
   sum=sum+x
print("The sum of the list is:",sum)
   

                #this is not support to string data type
#list=[1,2,3,4,5,6,"bhoo",7,8,9,10]      #by defualt it take index value 0
#sum=0             
#for x in list:
# sum=sum+x
#print("The sum of the list is:",sum)

name="laxmi"  #01234
for i in name:
   print(i)

name="laxmi"  
newname="kumari"
for i in name:
   if i not in newname:
       newname += i
print(newname)


roll_no=[3,5,7,1,11,4,5,2]
for x in roll_no:
   if x==2 or x==4 or x==6 or x==8 or x==10:
       print("even number =",x)
       break

#s.replace(old string,new string)
#inside s,every occurance of old string will be replaced by new string and return a new string
s=""
s1=s.replace("difficult","easy")
print(s1)
#All occurance will be replaced
s="ababaabababababaaabbb"
s1=s.replace("b","a")
print(s1)

x=['A','B','C']
y=['A','B','C']
#Z=[1,2,3,4]          #it won't compare the string and data type of x and z
print(x==y)           #it will compare the value of x and y
#print(x==z)
#print(x != z)        #it will compare the value of x and z

#index() method is used to find the index of the specific value in the list. It returns the index of the first occurrence of the specified value. If the value is not found, it raises a ValueError.
val=[1,2,3,5,5,5,1,2,4,4,6,6,6]
print(val.index(1))
print(val.index(2))
print(val.index(3))
print(val.index(4))
print(val.index(5))
print(val.index(6))

#count() method is used to count the number of occurrences(how many times it repeated in the list) of a specific value in the list. It returns the count of the specified value. If the value is not found, it returns 0.
print(val.count(1))  
print(val.count(2))
print(val.count(3))
print(val.count(4))
print(val.count(5))
print(val.count(6))

       

                            #import FUNCTION
import datetime
#datetime formatting
date=datetime.datetime.now()
print("It's now:{:%d-%m-%Y %H:%M:%S}".format(date))

