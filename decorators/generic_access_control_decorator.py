from functools import wraps


def get_current_user_role():
    return 0


def access_control(access_level):
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kv_args):
            if get_current_user_role() <= access_level:
                return func(*args, **kv_args)
            raise PermissionError('You do not have the proper access level.')
        return inner_wrapper
    return outer_wrapper


@access_control(access_level)
def delete_file(filename):
    print(f'{filename} is deleted!')


print(delete_file.__name__)
