import sys
def doSomething(input1,input2):
    multiple = [(input2*i)%10 for i in range(10)]
    
    res_digit = input1%10
    if (res_digit == 0):
        return 1
        
    for i in range(len(multiple)):
        if (multiple[i] == res_digit):
            return i
    return -1
inputVal = input()    
outputval = doSomething(int(inputVal.split()[0]),int(inputVal.split()[1]))

print (outputval)
