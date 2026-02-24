import datetime
import functools

def track_access(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().isoformat()
        print(f"Accessing {func.__name__} at {timestamp} with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def permission_check(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Assume first arg after self is user_role (for demo; in real use, pass role)
            user_role = kwargs.get('user_role', args[1] if len(args) > 1 else None)
            if user_role != required_role:
                raise PermissionError(f"Requires '{required_role}' role, got '{user_role}'.")
            return func(*args, **kwargs)
        return wrapper
    return decorator
