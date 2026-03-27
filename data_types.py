#Data types
                                    # list DATA TYPE
                                         
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52, "prashant"]  
print(mylist)  
print(type(mylist))  
print(mylist[0])  
print(mylist[1])   
print(mylist[2])  
print(mylist[-1])  
print(mylist[2:5])  
print(mylist[:5])   
print(mylist[1:])  
print(mylist[1:8:2]) #2 is increment,it will print 1,3,5,7 index value up to 8-1=7
print(mylist[:])
print(mylist[::-1]) # prints the list in reverse order



#how to change the index value
mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52, "prashant"]  
print(mylist) 
mylist[2]="Akshay"
print(mylist)


if "ankush" in mylist:
   print("Yes, ankush is available")
else:    
   print("No, ankush is not available")


mylist.append('harsh')
mylist.append("laxman")
print(mylist)


#if we have to add the value at specified index
mylist.insert(1,"sanket")
print(mylist)


mylist.remove("sandip")        #it will remove only first occurrence of sandip
print(mylist)

newlist=mylist.copy()  #it will create a copy of mylist and assign it to newlist
print(mylist)
print(newlist)


mylist = [ [ 'prashant',  'jha' ], [ '85.56' ], [ 440022, "yyy" ] ]      
print("example of multidimensional list: ")      
print(mylist)      
       #print(mylist[row][col])   #first square bracket represent row and second represent col      
print(mylist[0][0])  #prashant    
print(mylist[0][1])  #jha    
print(mylist[1][0])  #85.56
print(mylist[2][0])  #440022
print(mylist[2][1])  #yyy


list1=["prashant","jha"]
print(list1*2)  #it will print the list two times
list2=[50,25,50]
print(list1+list2) #it will concatenate the two list and print the result


list2=[50,25,50,'prashant']
del list2[2]  #it will delete the value at index 2
print(list2)

#del list2[2] 
#del list2          #it will delete the entire list2
#print(list2)       #it raises error

list2.clear()  #it will clear the list2 but it will not delete the list2
print(list2)   #[]

# List typecasting using 'list()' function  
name = "prashant"     #str
print(name)           # Output: prashant  
myname =list(name)   #type casting
print(myname)         # Output: ['p', 'r', 'a', 's', 'h', 'a', 'n', 't']  
# we have used list constructor 

#Reversing a list using 'reverse()' function  
list3 = [40, 30, 20, 10]  
list3.reverse()  
print(list3)  # Output: [10, 20, 30, 40]  
  
# Sorting a list using 'sort()' function
list4 =[44,22,77,0,9,88] #0,9,22,44,77,88
list4.sort() #it will sort the list in ascending order by default #sort(reverse=True) it will sort the list in descending order
print(list4)  # Output: [0, 9, 22, 44, 77, 88]
#defualt sorting order for numbers is ascending 
# default sortfor string is alphabetical order
#we should know that list should contain homogeneous data otherwise we will get typeerror

newlist =list4
print(id(newlist))
print(id(list4))  #both newlist and mylist are pointing to the same list in memory location



                              # tuple DATA TYPE

mytuple=("prshant","ashish","rahul","sandip","komal","ankush","rajesh",23,3.25,"sandip")
print(mytuple)
print(type(mytuple))

print(mytuple[0])

#mytuple[0]="sunil" #tuple is immutable we cannot change the value of tuple
#print(mytuple)

     #differnce between list and tuple
     #if we want to store data which is changeable we will use list data type 
     #if we want to store data which is not changeable we will use tuple data type




                                        # set DATA TYPE

myset = {1, 2, "sanjay", 5.66, "rahul", "ayush", "ramesh", "ankit", "rishikesh"}  
print("Output:", myset)  
# Output: {'ayush', 1, 2, 'rishikesh', 5.66, 'ramesh', 'sanjay', 'ankit', 'rahul'}  
print(type(myset))

myset.add(60)
print(myset)

#myset.remove(3)   #if we 100% sure that the element is present in the set then we can use remove() method to remove the element from the set
#print(myset)

myset.discard(3)     #if we are not sure that the element is present in the set then we can use discard() method to remove the element from the set
print(myset)

myset={10,20,30,40}
yourset={"prashanta","jha"}
newset=myset.union(yourset) #union() method is used to combine two sets and return a new set that contains all the elements from both sets. It does not modify the original sets.
print(newset)

#intersection return common element from both sets
myset={10,20,30,40}
yourset={10,30,50,60}
print(myset.intersection(yourset))  #intersection() method is used to find the common elements between two sets. It returns a new set that contains only the elements that are present in both sets. It does not modify the original sets.

print(myset.difference(yourset))    #difference() method is used to find the elements that are present in one set but not in the other. It returns a new set that contains only the elements that are present in the first set but not in the second set. It does not modify the original sets.
print(yourset.difference(myset))    #difference() method is used to find the elements that are present in one set but not in the other. It returns a new set that contains only the elements that are present in the first set but not in the second set. It does not modify the original sets.

      #clear() we can use to clear data 
      #pop() method is used to remove object
#myset={10,20,30,40}
#print(myset.pop()) 
#print(myset.clear())



                                        #Dictionary DATA TYPE

mydict={
   "name":"laxmi",
  "profession":"student",
 "age":20,
}
print(mydict)
print(type(mydict))

mydict={
    101:"laxmi",
    102:"prashant",
    103:"ashish",
    104:"rahul",
}
print(mydict)


mydict={
    101:"laxmi",
    102:"prashant",
    103:"ashish",
    104:"rahul",
    101:"sandip",
    104:"pinky"
}
print(mydict)

#with the help of key we have to print values
a=mydict[102]
print(a)

#we will replace the old value by ne\w value
mydict[102]="komal"
print(mydict)

#Only print the key x=0,1
for x in mydict:
    print(x)

#Only print the values
for x in mydict.values():
    print(x)

#print both key and value
for x,y in mydict.items():
    print(x,y)

#if I have to add new key and value in dictionary
mydict["mobile_no"]=1234567890
print(mydict)

#pop method is used to remove the key and value from the dictionary
mydict.pop(101)
print(mydict)

newdict=mydict.copy()  #copy method is used to copy the dictionary
print(newdict)

