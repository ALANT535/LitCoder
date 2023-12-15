import sys
def doSomething(arr,k,n):
    
    res = []
    
    for i in range(len(arr)-k+1):
        temp_list = arr[i:i+k]
        temp_list.sort()

        
        res.append(temp_list[n-1])

    
    return res
    
input1 = list(map(int,input().split(" ")))
input2 = int(input())
input3 = int(input())

output1 = doSomething(input1,input2,input3)
for value in output1:
    print(value,end = " ")
                                                                                                                            
