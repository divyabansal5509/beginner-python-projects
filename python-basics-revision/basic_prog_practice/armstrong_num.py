
def is_armstrong(num):
    digits = str(num)
    digits_count = len(digits)
    total=0
    for digit in digits:
        total += int(digit)**digits_count
    return total == num

print(is_armstrong(153))

print(is_armstrong(720))

print(is_armstrong(9442))