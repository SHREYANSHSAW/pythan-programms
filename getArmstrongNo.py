# lowerlimit = int(input("give  the lowest no. of "))
# upperlimit = int (input("enter the upper limit"))

# for num in range  (lowerlimit, upperlimit+1):
#    order = len(str(num))
#    sum = 0 
#    temp = num

# while temp > 0:
 
#  digit = temp % 10
#  sum += digit**order
#  temp //= 10

# if num == sum:
#             print( num)
# else:
#             print("its not armastrong no.")

lowerlimit = int(input("give your lower limit"))
upperlimit = int(input("give your upper limit"))

for num in range(lowerlimit, upperlimit+1):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp%10
        sum += digit**order
        temp //= 10
        if num == sum:
            print(num)


           

