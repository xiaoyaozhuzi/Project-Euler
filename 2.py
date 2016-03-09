def feb(i):
    if i == 0 or i == 1:
        return 1
    else:
        result = feb(i-1) + feb(i-2)
        return result
 
sum = 0
i = 0
tmp = 0
while tmp < 4000000:
    i += 1
    tmp = feb(i)
    if not tmp % 2:
        sum += tmp
print(sum)
