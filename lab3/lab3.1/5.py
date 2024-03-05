
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers in the list:", prime_numbers)