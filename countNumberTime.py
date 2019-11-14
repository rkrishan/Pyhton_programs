def countAnumberWithDigit(n):
    count = 0

    for i in range(n+1):
        if(hasXDigit4(i)==True):
            count +=1

    return count




def hasXDigit4(x):
    while(x!=0):
        if(x%10==5):
            return True
        x = x/10
    return False


val = countAnumberWithDigit(20)

print(val)
