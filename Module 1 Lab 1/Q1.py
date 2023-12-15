import sys
def doSomething(inval):
    lower = upper = number = other = 0
    n = len(inval)
    for i in inval:
        if i.isalpha():
            if i.isupper():
                upper += 1
            else:
                lower += 1
        elif i.isalnum():
            number += 1
        
        else:
            other += 1
        
        
            
    l1 = [upper/n,lower/n,number/n,other/n]
    
    
    return [str(round(i*100,3))+"%" for i in l1]
    
    
inputVal = input()    
outputVal = doSomething(inputVal)
print ("\n".join(outputVal))
