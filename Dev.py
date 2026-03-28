new_dict = {}
while True:
    print(new_dict)
    x = input("Would you like to create a new key value pair: ").lower()
    if x == 'yes':
        d = input("Would you like your value to be a string or a number: ")
        if d=='string':
            y = input("Does this key have multiple values: ").lower()
            if y == "yes":
                z = input("What is the key: ").lower()
                v = int(input("How many values would you like to add: "))
                j = []
                for i in range (v):
                    b = input(f'{i+1} value: ')
                    j.append(b)
                new_dict[z]=j 
            elif y =="no":
                a = input("What would you like your key to be: ").lower()
                c = input("What would you like your value for the key to be: ").lower()
                new_dict[a]=c
        if d == "number":
            y = input("Does this key have multiple values: ").lower()
            if y == "yes":
                e = input("What is the key: ")
                f = int(input("How many values would you like to add: "))
                g = []
                for i in range (f):
                    b = input(f'{i+1} value: ')
                    g.append(b)
                new_dict[e]=g 
            elif y =="no":
                h = input("What would you like your key to be: ")
                k = int(input("What would you like your value for the key to be: "))
                new_dict[h]=k        
    elif x == "no":
        break
print('This is your dictionary',new_dict)