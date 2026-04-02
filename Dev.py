stack = [5, 4, 6, 7]
def push(a):
    stack.append(a)
    
push(8)
print(stack)



s = [5, 1, 3, 4, 7]
def s_pop(s):
    if len(s)==0:
        return None
    return s.pop()
    
for i in range(6):
    s_pop()
print(s)



def empty(stack2):
    return len(stack2)==0


stack4 = []
def push(b):
    stack4.append(b)

push(5)
push(7)
push(2)
push(4)
s_pop(stack4)
push(8)
push(1)
push(1)
push(3)    
s_pop(stack4)                                                                                                     
   

    