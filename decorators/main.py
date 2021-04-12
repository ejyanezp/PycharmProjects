import functools

# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


# You code starts here:
# Define a check_permission() decorator:
def check_permission(func):
    @functools.wraps(func)
    def wrapper():
        if user.get('role') == 'admin':
            func()
        else:
            raise PermissionError('You are not admin.')
    return wrapper


@check_permission
def delete_database():
    print('Database deleted!')


# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:
secure_delete_database = check_permission(delete_database)
secure_delete_database()

print(delete_database.__name__)
