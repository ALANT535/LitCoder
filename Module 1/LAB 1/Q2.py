import sys
def doSomething(inval):
    l = inval.split()
    n1 = len(l)
    max1 = -9999999
    for i in range(len(l) - 1):
        for j in range(i+2,n1+1,2):
            temp_l = l[i:i+j]
            
            if temp_l.count('0') == temp_l.count('1'):
                print("j is ",j,"\ntemp_l is ",temp_l)
                max1 = max(max1,len(temp_l))
        
        
    
    
    
    return max1
    
inputVal = input()    
outputVal = doSomething(inputVal)
print (outputVal)


l = [1,2,3]
l1 = l[1:] + [l[0]] 
l = l1
