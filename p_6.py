def main():
    s=input("enter first list").split()
    test1=[str(x) for x in s]
    test3=firstVowel(test1)
    for str1 in test3:
       print (str1 ,end=" ")
def firstVowel(lst):
    test2=[]
    for str1 in lst:
        k=0
        for alpha in str1:
            if alpha=='a' or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u':
                str2=pigLatin(str1,k)
                test2.append(str2)
                break
            k=k+1
    return test2
def pigLatin(str1,k):
    test2=[]
    if k==0:
        str2=str1+"yay"
        return str2

    else:
        str2=str1[k:len(str1)]+str1[0:k]+"ay"
        return str2

main()
    



