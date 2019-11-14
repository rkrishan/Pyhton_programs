def OccurnaceOf5Inrange(n):
    count = 0

    while(n>0):
        if(n%10==5):
            count +=1
        n = n/10

    return count


def numberOf5InRange(n):
    count = 0

    for i in range(5,n+1):
        count = count+OccurnaceOf5Inrange(i)

    return count



print(numberOf5InRange(100))            
