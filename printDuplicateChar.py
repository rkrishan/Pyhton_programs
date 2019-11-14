no_of_char = 256

def fillcharCount(stng,count):
    for i in stng:
        count[ord(i)] +=1
        print(count[ord(i)])
    return count

def printDuplicateChar(strng):

    count = [0]*no_of_char

    count = fillcharCount(strng,count)

    k = 0

    for i in count:
        if int(i)>1:
            print(chr(k),", count ="+str(i))
        k +=1

string = "test string"
print (printDuplicateChar(string))
