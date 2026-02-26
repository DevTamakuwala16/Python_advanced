n = []

n.append(0)
n.append(1)
n.append(2)
for i in range(2):
    x=int(input("Enter a number: "))
    n.append(x)

del n[3] 
del n[3]  
n.insert(0, 4)

for i in range(len(n)):
    t += n[i]
    print(t)

