import sys
def doSomething(inval):
    stack1 = []
    stack2 = []
    for i in inval:
    #3 possible cases
        if (i[0]=="1"):
            val = int(i.split()[1])
            stack1.append(val)
        
        elif (i[0]=="2"):
            while (len(stack1)!=0):
                stack2.append(stack1.pop())
            stack1 = []
            popped_element = stack2.pop()
            
            while (len(stack2)!=0):
                stack1.append(stack2.pop())
            stack2 = []
       
        
        elif (i[0]=="3"):
            while (len(stack1)!=0):
                stack2.append(stack1.pop())
            stack1 = []
            
            while (len(stack2)!=0):
                temp = stack2.pop()
                print(temp,end = " ")
                stack1.append(temp)
            stack2 = []
            print("")
        
    
    return 0
inputVal = input().split(",")
outputVal = doSomething(inputVal)
