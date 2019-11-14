def compress(strng):
    res= ""
    count = 1

    res +=strng[0]

    for i in range(len(strng)-1):
        if(strng[i]==strng[i+1]):
            count += 1
        else:
            if(count>1):
                res += str(count)
            res +=strng[i+1]
            count =1 
    if(count>1):
        res += str(count)     
    return res 

val= compress("ddaaaffddpaa")                  
print(val)
