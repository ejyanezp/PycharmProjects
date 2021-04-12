import time


def powers(limit: int):
    return [i**2 for i in range(limit)]


start = time.time()
powers(5000000)
end = time.time()

print(end-start)
