import sys


def doSomething(input1):
    
    for i in range(0,len(input1) - 1):
        
        for j in range(i+1,len(input1)):
            
            if input1[i] == input1[j]:
                continue
            
            elif input1[i] in input1[j] or input1[j] in input1[i]:
                return "BAD PASSWORD"
            
    
    return "GOOD PASSWORD"

input1 = list(input().split())
output1 = doSomething(input1)
print (output1)
                                                                                                                            
