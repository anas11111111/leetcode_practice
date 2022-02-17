def divide(dividend, divisor):
    MAX_VALUE = 2**31 - 1
    MIN_VALUE = -2**31

    if divisor == 0 or (divisor == -1 and dividend == MIN_VALUE):
        return MAX_VALUE

    q = 0
    sign = 1
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        sign = -1

    while dividend >= divisor:
        shift_l = 0
        while dividend >= (divisor << shift_l):
            shift_l = shift_l + 1

        q = q + (1 << (shift_l-1))
        dividend = dividend - (divisor << (shift_l-1))

    return -q if sign == -1 else q


res = divide(22, 3)
print(res)
