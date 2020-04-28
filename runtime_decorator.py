def my_timer(origional_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = origional_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} seconds'.format(origional_function.__name__, t2))
        return result

    return wrapper
