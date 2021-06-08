def digit_of_life(n):
    sum = 0
    while int(n) >= 10:
        for i in n:
            sum += int(i)
        n = str(sum)
        sum = 0
    return n

n = input('Enter birthday (YYYYMMDD):')
print(digit_of_life(n))
