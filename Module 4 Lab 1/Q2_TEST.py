import sys
def egypt(a,b):
    
    a1,b1 = a,b
    res = []
    diff_a,diff_b = a,b
    so_far_a,so_far_b = 0,1
    
    while diff_a!=0:
        
        temp = diff_a / diff_b
        if (temp.is_integer()):
            res.append(temp)
            break
        
        res_temp = b//a + 1
        res.append(res_temp)
        
        so_far_a = (res_temp * so_far_a + so_far_b * 1)
        so_far_b = (res_temp * so_far_b)
        
        
        diff_a = (a1 * so_far_b - so_far_a * b1)
        diff_b = (b1 * so_far_b)
        print(a1*so_far_b-so_far_a*b1)
        print("diff_a ",diff_b)
        
        print("difference between ",a1," / ",b1," and ",so_far_a," / ",so_far_b," is ",diff_a," / ",diff_b)
        
    
    return res
    

input1 = int(input())
input2 = int(input())
output1 = egypt(input1,input2)
print (output1)
                                                                                                                            
