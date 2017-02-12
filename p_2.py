n1,n2=eval(input("enter two number"))
if n1>n2:
    print(n1+n2)
elif n1<n2:
    if 10%n2==0:
        print(n1*n2)
    else:
        print(n1/n2)
