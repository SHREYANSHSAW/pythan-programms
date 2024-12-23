a =0
b=1

num = int(input("give your no. to know fibnocci series"))
if a == 1:
    print(a)
    
else:
    print(a)
    print(b)
    for i in range(2,num+1):
        c = a+b
        b = a
        a = c
        print(c)
    