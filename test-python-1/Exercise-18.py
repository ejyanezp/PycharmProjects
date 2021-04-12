def prime_generator(bound):
    for n in range(2, bound):
        for i in range(2, 1 + n // 2):
            if n % i == 0:
                break
        else:
            yield n


gen = prime_generator(30)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
