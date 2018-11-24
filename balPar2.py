opn = []
clc = []

def bal(strin):
    oC = 0
    cC = 0
    for i in strin:
        if i == "(":
            oC =+ 1
            opn.append(i)
        elif i == ')':
            cC += 1
            clc.append(i)
    
    #print oC, cC
    if len(opn) > len(clc):
        for i in range(len(opn)-len(clc)):
            clc.append(')')
    elif len(clc) > len(opn):
        for i in range(len(clc) - len(opn)):
            opn.append('(')

    #print opn
    #print clc
    nlist = opn+clc
    strin = ('').join(nlist)
    print strin


bal("(())(())))))")