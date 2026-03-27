# condional statements
# conditional statements are used to perform different actions based on different conditions.
# simple if and elif and else
# WAP to accept one single digit and check the entered number is positive or negative or zero
N = int(input("Enter a single digit: "))
if N > 0:
    print("The number is positive.")
if N < 0:
    print("The number is negative.")
if N == 0:
    print("The number is zero.")


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

#1.  rstrip() ====> removes spaces at right side of the string
#2.  lstrip() ====> removes spaces at left side of the string
#3.  strip()  ====> removes spaces at both sides of the string

programming=input("Eter your programming Name:")
p_name=programming.strip()
if p_name == "Python":
    print(p_name)
elif p_name == "Java":
    print(p_name)
elif p_name == "Cpp":
    print(p_name)
else:
    print("Wrong Programming Name")


