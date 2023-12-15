import sys
def clumsy(input1):
    m = ["add","sub","mul","div"]
    
    res = 0
    
    if input1 <=3:
        return input1
    
    else:
        res += (inpu1t[0] * input1[1]) // input1[2]
        
 
    res_add,res_sub = 0,0
        
    
    for i in range(3,len(input1),4):
        res_add += input1[i]
        
        if (i+3<len(input1)):
            res_sub += input1[i+1] * input1[i+2] // input1[i+3]
        
        elif (i+2<len(input1)):
            res_sub += input1[i+1] * input1[i+2]
        
        elif (i+1<len(input1)):
            res_sub += input1[i+1]
        
        else:
            break
        
        
    res += res_add
    res -= res_sub
    
    return res
    
    
inputVal = int(input())

output1 = clumsy(input)
print (output1)
                                                                                                                            
