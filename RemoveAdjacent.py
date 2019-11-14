
def removeAdjacent(s):
    n = len(s)

    if (n<2):
        return
    j =0

    for i in range(n):
        if(s[j]!=s[i]):
            j +=1
            s[j]= s[i]

    j +=1
    s = s[:j]
    return s

if __name__ == '__main__':
    S1 = "geeksforgeeks"
    S1 = list(S1)
    print(S1)
    S1 = removeAdjacent(S1)
    print(*S1, sep = "")
