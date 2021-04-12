import collections


def test_any(x):
    if any(x):
        print("hello any")
    if x:
        print("Hello collection")


b = [None, None, None, 1]
c = [None, None, None]
test_any(b)
test_any(c)

my_int = 5
print(id(my_int))
d = my_int
print(id(d))
d = 9
print(id(d))

cnt = collections.Counter()
my_list = ['red', 'blue', 'green', 'red', 'blue', 'red']
for word in my_list:
    cnt[word] += 1
print(cnt)
print(my_list[-1])
print(my_list[-2])

my_dict = {'index': 1, 'timestamp': '2021-04-07 10:10:00', 'proof': 234, 'previous_hash': 'abcdef1234567890'}
print(repr(my_dict))
