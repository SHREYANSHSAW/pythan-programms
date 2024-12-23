def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))
    
num = int(input("enter a number here:"))
result = fact(num)
print("fact of given no. is", result)