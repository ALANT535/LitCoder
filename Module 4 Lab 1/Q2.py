import sys
def manip(arr,input):
    
    start = input[0]
    end = input[1]
    val = input[2]
    
    for i in range(start-1,end):
        arr[i] += val
    
    
    
    return arr
    
    
    
n = int(input())
arr = [0] * n
m = int(input())

for i in range(m):
    input1 = list(map(int,input().split()))
    arr = manip(arr,input1)



arr.sort()
print(arr[-1])
                                                                                                                            
