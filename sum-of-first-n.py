def sumOfFirstNFunctional(N):
    if N==0:
        return 0
    return N+sumOfFirstNFunctional(N-1)    
print(sumOfFirstNFunctional(100))


  
def sumOfFirstNParamiterised(i,sum):
    if i==0:
        print(sum)
        return
    sum+=i
    sumOfFirstNParamiterised(i-1,sum)
sumOfFirstNParamiterised(100,0)
