from paramiko.ssh_exception import AuthenticationException


def auth(fn):
    def wrapper(*args, **kwargs):
        try:
            fn(*args, **kwargs)
        except AuthenticationException:
            print("Auth error")
    return wrapper
