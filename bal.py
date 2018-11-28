leftB = []
rightB = []
leftC = []
rightC = []
leftcount = 0
rightcount = 0
strinArray = []
resArray = []
posCounter = []
pos = 0
final = []
res = ""

def main(strin):
    global pos, leftcount, rightcount

    for paren in strin:
        strinArray.append(paren)
    
    for pos, paren in enumerate(strinArray):
        if paren == "(":
            posCounter.append(pos)
            resArray.append(paren)
            #print index, paren
            leftcount += 1
        elif paren == ")":
            posCounter.append(pos)
            resArray.append(paren)
            #print index, paren
            rightcount += 1

    # print("Before op")
    # print("Res Array: {}, len:{}".format(resArray, len(resArray)))
    # print("Pos counter: {}, len;{}".format(posCounter, len(posCounter)))
    # print("final: {}".format(final))
    
    #finding the innermost and balanced pair(s)
    for i in range(rightcount-1):
        for pos, paren in enumerate(resArray):
            if paren == ")":
                if resArray[pos-1] == "(":
                    final.insert(0, resArray[pos-1])
                    resArray.remove(resArray[pos-1])
                    final.insert(1, paren)
                    resArray.remove(paren)
    

            
            
            # if paren == ")" and pos == index + 1:
            #     print("Second if")
            #     print(paren, pos, index)
            #     if resArray[pos - 1] == "(":
                    
            #         final.insert(0, resArray[pos-1])
            #         final.append(paren)
            #         resArray.remove(resArray[pos -1])
            #         resArray.remove(paren)
            #         posCounter.remove(pos)
            #         posCounter.remove(pos -1)
            
            # if paren == ")" and pos == index -1:
            #     print("third if")
            #     print(paren, pos, index)
            #     if resArray[pos - 1] == "(":
                    
            #         final.insert(0, resArray[pos-1])
            #         final.append(paren)
            #         resArray.remove(resArray[pos -1])
            #         resArray.remove(paren)
            #         posCounter.remove(pos)
            #         posCounter.remove(pos -1)
    
    


    for pos, paren in enumerate(resArray):
        for index in posCounter:
            if paren == ")" and index == pos:
                final.insert(0, "(")
                final.append(paren)
                resArray.remove(paren)
                resArray.remove(resArray[pos-1])
                posCounter.remove(index)
            
    #checking if the last is an opener or closer
    for pos, paren in enumerate(resArray):
        if paren == "(" and pos == len(resArray) - 1:
            final.append(paren)
            final.append(")")
            resArray.remove(paren)
            
        elif paren == ")" and pos == len(resArray) -1:
            final.insert(0, "(")
            final.append(paren)
            resArray.remove(paren)
            #posCounter.remove(index)


    for paren in resArray:
        final.insert(0, paren)
        final.append(")")
        #resArray.remove(paren)

    res = ("").join(final)
    # print
    # print("After operation")
    # print "Position counter: {}, len: {}".format(posCounter, len(posCounter))
    # print leftcount, rightcount
    print "final: {}".format(final)

    print "result array: {}, len:{}".format(resArray, len(resArray))
    print strin
    print res
    # print(len(strin))
    # print(len(res))
if __name__ == "__main__":
    main("((()(")