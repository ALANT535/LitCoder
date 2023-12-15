import sys

def cookies(input1,input2):
    counter = 0
    input2.sort()
    min_elem = input2[0]
    while (min_elem < input1):
        
        input2.append(input2[0] + 2*input2[1])
        input2 = input2[2:]
        input2.sort()
        
        min_elem = input2[0]
        
        counter += 1    
    
    return counter
    
target_sweet = int(input())
sweets = list(map(int,input().split()))



output1 = cookies(target_sweet,sweets)
print (output1)
                                                                                                                            
