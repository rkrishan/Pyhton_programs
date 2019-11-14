def printFab(n):

    if(n<=0):
        print("put postive number")
    elif(n==1):
        print(0)
    else:
        n1 = 0
        n2 = 1
        count = 0

        while(count<n):
            print(n1,end=' ')
            nth = n1+n2
            n1 = n2
            n2 = nth

            count +=1

if __name__ == "__main__":
    nterms = int(input("How many terms? "))
    printFab(nterms)
                
            





    





