# packaging examples
def add_all(*args):
    return sum(args)


def pretty_print(**kv_args):
    for k, v in kv_args.items():
        print(f'For {k} there is {v}.')


# Unpackaging examples
def add_arg(a1, a2, a3, a4, a5):
    return a1 + a2 + a3 + a4 + a5


def print_access_level(username: str, access_level: str):
    print(f'User {username} has access level {access_level}.')


# Packaging arguments example
print(add_all(1, 2, 3, 4, 5))
pretty_print(username='jose123', access_level='admin')

# Unpackaging collections example
my_tuple = (1, 2, 3, 4, 5)
print(add_arg(*my_tuple))

# when unpackaging a dictionary,
# the dict keys must match with the parameter names (using named arguments)
my_dict = {'username': 'jose123', 'access_level': 'admin'}
print_access_level(**my_dict)
