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