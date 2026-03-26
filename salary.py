#WAP to calculate gross salary from basic salary(HRA=30% ,TA=40% ,DA=20%)
basic=float(input("Enter Basic Salary:"))
gross=basic+(0.3*basic)+(0.4*basic)+(0.2*basic)
print("Gross Salary =",gross)