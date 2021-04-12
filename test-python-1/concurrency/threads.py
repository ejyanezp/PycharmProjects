import time
from threading import Thread


def ask_user():
    loc_start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - loc_start)


def complex_calculation():
    print('Started calculating...')
    loc_start = time.time()
    [x**2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - loc_start)


# With a single thread, we can do one at a time—e.g.
print('# SINGLE THREAD')
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')


print('# TWO THREADS')
# With two threads, we can do them both at once...
thread = Thread(target=complex_calculation)  # the function that computes first
thread2 = Thread(target=ask_user)  # Put the function that waits last

start = time.time()

thread.start()
thread2.start()

thread.join()
thread2.join()

print('Two thread total time: ', time.time() - start)