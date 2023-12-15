import sys


class customstack:
    def __init__(self):
        self.stack = [""]
        self.top = 0
    
    
    def insert(self,value):
        res = self.stack[self.top] + value
        
        self.stack.append(res)
        self.top += 1
        
        
    def delete(self,value):
        res = self.stack[self.top][:len(self.stack[self.top]) - value]
        
        
        self.stack.append(res)
        self.top += 1
    
    
    def get(self,value):
        return self.stack[self.top][value-1]
        
    
    def undo(self):
        
        self.stack = self.stack[:-1]
        self.top -= 1
        
    


def doSomething(inval):
    
    stack1 = customstack()

    
    split = inval.split(",")
    for i in split:
        if i[0]=="1":
            
            value = i.split()[1]
            
            stack1.insert(value)

            
            
        elif i[0]=="2":
            value = int(i.split()[1])
            
            stack1.delete(value)

       
        elif i[0]=="3":
            
            value = int(i.split()[1])
            
            print(stack1.get(value))
            
        elif i[0]=="4":
            stack1.undo()
            
            value = i.split()[1]

    return "done"
    
    
    
inputVal = input()    
outputVal = doSomething(inputVal)
# print (outputVal)
                                                                                                                            
