sum_of_digits = lambda n: sum(int(digit) for digit in str(n) if digit.isdigit())
num = (12345)
result = sum_of_digits(num)

print("sum of digits:", result)