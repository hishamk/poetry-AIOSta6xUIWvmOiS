def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Prime numbers up to 2000:")
    primes = [n for n in range(2, 2001) if is_prime(n)]
    print(primes)
