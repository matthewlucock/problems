def once(function):
    function_has_been_called = False

    def wrapper(*args, **kwargs):
        if not function_has_been_called:
            function_has_been_called = True
            return wrapper(*args, **kwargs)

    return wrapper
