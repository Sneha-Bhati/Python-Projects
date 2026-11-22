# Practical 02: Check whether a number is prime
n = int(input("Enter an integer: "))

if n < 2:
    print(n, "is not a prime number.")
else:
    is_prime = True
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            is_prime = False
            break
    print(n, "is a prime number." if is_prime else "is not a prime number.")
