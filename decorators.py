# let's review python decorators
def decorator_function(origional_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper exectued this before {}'.format(origional_function.__name__))
        return origional_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, origional_function):
        # this ties our functino with an instance of this decorator_class
        self.origional_function = origional_function

    def __call__(self, *args, **kwargs):
        print('call exectued this before {}'.format(self.origional_function.__name__))
        return self.origional_function(*args, **kwargs)


@decorator_class
def display():
    print('display function ran')

# we dont need the two lines below if we add the syntax of @decorator_function
# decorated_display = decorator_function(display)


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Aaron', 34)

display()
