#mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52, "prashant"]  
#print(mylist)  
#print(type(mylist))  
#print(mylist[0])  
#print(mylist[1])   
#print(mylist[2])  
#print(mylist[-1])  
#print(mylist[2:5])  
#print(mylist[:5])   
#print(mylist[1:])  
#print(mylist[1:8:2]) #2 is increment,it will print 1,3,5,7 index value up to 8-1=7
#print(mylist[:])
#print(mylist[::-1]) # prints the list in reverse order



#how to change the index value
#mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip" , 60.52, "prashant"]  
#print(mylist) 
#mylist[2]="Akshay"
#print(mylist)




#if "ankush" in mylist:
#    print("Yes, ankush is available")
#else:    
 #   print("No, ankush is not available")




#mylist.append('harsh')
#mylist.append("laxman")
#print(mylist)


             #if we have to add the value at specified index
#mylist.insert(1,"sanket")
#print(mylist)


#mylist.remove("sandip")        #it will remove only first occurrence of sandip
#print(mylist)

#newlist=mylist.copy()  #it will create a copy of mylist and assign it to newlist
#print(mylist)
#print(newlist)


#mylist = [ [ 'prashant',  'jha' ], [ '85.56' ], [ 440022, "yyy" ] ]      
#print("example of multidimensional list: ")      
#print(mylist)      
       #print(mylist[row][col])   first square bracket represent row and second represent col      
#print(mylist[0][0])  #prashant    
#print(mylist[0][1])  #jha    
#print(mylist[1][0])  #85.56
#print(mylist[2][0])  #440022
#print(mylist[2][1])  #yyy


#list1=["prashant","jha"]
##print(list1*2)  #it will print the list two times

#list2=[50,25,50]
#print(list1+list2) #it will concatenate the two list and print the result


#list2=[50,25,50,'prashant']
#del list2[2]  #it will delete the value at index 2
#print(list2)

#del list2[2] 
#del list2   #it will delete the entire list2
#print(list2)

#list2.clear()  #it will clear the list2 but it will not delete the list2
#print(list2)   #[]

         # List typecasting using 'list()' function  
#name = "prashant"  #str
#print(name)  # Output: prashant  
#myname = list(name)  #type casting
#print(myname)  # Output: ['p', 'r', 'a', 's', 'h', 'a', 'n', 't']  
          #we have used list constructor 

          # Reversing a list using 'reverse()' function  
#mylist = [40, 30, 20, 10]  
#mylist.reverse()  
#print(mylist)  # Output: [10, 20, 30, 40]  
  
            # Sorting a list using 'sort()' function
mylist =[44,22,77,0,9,88] #0,9,22,44,77,88
#mylist.sort() #it will sort the list in ascending order by default #sort(reverse=True) it will sort the list in descending order
#print(mylist)  # Output: [0, 9, 22, 44, 77, 88]
           #defualt sorting order for numbers is ascending 
           # default sortfor string is alphabetical order
           #we should know that list should contain homogeneous data otherwise we will get typeerror

#newlist =mylist
#print(id(newlist))
#print(id(mylist))  #both newlist and mylist are pointing to the same list in memory location
