def main():
    s=input("enter first list").split()
    test1=[int(x) for x in s]
    d=input("enter second list").split()
    test2=[int(x) for x in d]
    test3=interLeave(test1,test2)
    print(test3)

def interLeave(lst1,lst2):
    test3=[]
    if len(lst1)>=len(lst2):
        for i in range(len(lst2)):
            test3.append(lst1[i])
            test3.append(lst2[i])
        return test3

main()
