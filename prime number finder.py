def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

N = 50  #desired number
prime_numbers = [num for num in range(2, N + 1) if is_prime(num)]

print("number 1 to", N, ":", prime_numbers)
