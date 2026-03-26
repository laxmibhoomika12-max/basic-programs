#WAP to accept days and check the working day or weekend
day=int(input("Enter the day number: "))
if day >=1 and day<=5:
    print("It is a working day.")
if day == 6 or day == 7:
    print("It is a weekend.")




    #OR
day=input("Enter the day  ")
if day=="Sunday" or day=="sunday" or day=="Saturday" or day=="saturday" or day=="SUNDAY" or day=="SATURDAY":
    print("It is a weekend.")
else:
    print("It is a working day.")