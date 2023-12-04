import sys
def longest_substring(inval):
    
    counter = 0
    max_len = 0
    visited = []
    for i in inval:
        
        if i not in visited:
            visited.append(i)
            counter += 1
        
        else:
            visited = []
            max_len = max(max_len,counter)
            counter = 1
        
    
    max_len = max(max_len,counter)
    
    return max_len
    
    
inputVal = input()    
outputVal = longest_substring(inputVal)
print (outputVal)
                          
