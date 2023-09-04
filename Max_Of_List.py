number1=int(input("Enter a number"))
number2=int(input("Enter a number"))
number3=int(input("Enter a number"))
number4=int(input("Enter a number"))
number5=int(input("Enter a number"))
list=[]
i=number1
new_i=i
list=[number1,number2,number3,number4,number5]
for new_i in list:
    if (new_i>i):
        i=new_i

print("The biggest number is", i)
    
    
