#WAP to accept three paper marks and calculate total and percentage and if percentage is greater than equal to 60
math=60
chem=70
phy=60
total=math+chem+phy
percentage=total/3.0
print("Total Marks =",total)
print("Percentage =",percentage)
if percentage>=60:
    print("you are eligible for placement")
else:
    print("you are not eligible for placement")