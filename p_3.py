def main():
    s=input("enter first list").split()
    list1=[int(x) for x in s]
    list2=uniqueList(list1)
    print(list1)
    print(list2)


def uniqueList(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
main()
    



