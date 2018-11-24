from sys import argv

script, strin = argv


pair = {}
seq = []
nSeq = []

def checker(strin):
    for paren in strin:
        seq.append(paren)

    for index, item in enumerate(seq):
        # print(index, item)  
        if item == "(":
            nSeq.insert(index, item)
            nSeq.insert(index+1, ")")
        elif item == ")":
            nSeq.insert(index, item)
            nSeq.insert(index-1, "(")
    print nSeq   

checker(strin)