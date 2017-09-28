def power_digit_sum(n,i):
    power = n**i
    digit_sum = 0
    while power != 0:
        digit_sum += power % 10
        power //= 10
    return digit_sum

print(power_digit_sum(2,1000))
