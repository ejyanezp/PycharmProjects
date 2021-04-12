import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - start)


def complex_calculation():
    print('Started calculating...')
    start = time.time()
    [x**2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - start)


# TWO THREADS
print('# TWO THREADS')
# With two threads, we can do them both at once...
start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

# All this does is we don't have to call pool.shutdown()

print('Two thread total time: ', time.time() - start)
