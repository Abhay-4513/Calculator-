a = float(input("Enter first numebr : "))
b = float(input("Enter the second number : "))

Operation_1 = "+"
Operation_2 = "-"
Operation_3 = "*"
Operation_4 = "/"
Operation = input("Select the oparation '+','-', '*', '/': ")

if Operation == Operation_1:
    print(a+b)

elif Operation == Operation_2:
    print(a-b)

elif Operation == Operation_3 :
    print(a*b)
 
elif Operation==Operation_4 :
    print(a/b)

elif b==0 :
    print("Cannot divide by zero")
     
else:
    print("Select correct opration") 
