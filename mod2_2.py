a=int(input("Enter Value : "))

n=1

if a<0:
    print("PLS ENTER POSITIVE NUMBER!!")
elif a==0:
    print("FACTORIAL of 0 is 1.")
else:
    for i in range(1,a+1):
        n=n*i
    print("Factorial of ", a, " Is ", n)    
