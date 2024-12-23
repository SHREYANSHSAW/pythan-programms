num = int(input("put your to get the sum of below no."))

if num < 0:
    print("plese inter positive no.")
else:
    sum = 0
    while num> 0:
        sum += num
        num -= 1
        print(sum)


    