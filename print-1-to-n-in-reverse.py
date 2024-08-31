def printOnetoNinReverse(i,N):
    if i>N:
        return
    printOnetoNinReverse(i+1,N)
    print(i)

printOnetoNinReverse(1,5)   