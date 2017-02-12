def main():
    s=input("enter first list").split()
    list1=[int(x) for x in s]
    d=input("enter second list").split()
    list2=[int(x) for x in d]
    list3=inBoth(list1,list2)
    print(list1)
    print(list2)
    print(list3)

def inBoth(list1,list2):
    list3=[]
    for i in list1:
        if (i in list1) and (i in list2):
            list3.append(i)
    return list3
            

main()
    



