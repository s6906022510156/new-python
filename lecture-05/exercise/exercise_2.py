def generate_primes(n):
    primes = []

    for num in range(2, n + 1):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(str(num))

    return ", ".join(primes)


# Example usage
print(generate_primes(10))  # 2, 3, 5, 7
print(generate_primes(20))  # 2, 3, 5, 7, 11, 13, 17, 19
print(generate_primes(1))   # ""
print(generate_primes(2))   # 2
print(generate_primes(100))   # 2