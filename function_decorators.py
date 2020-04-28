# let's review python decorators
def decorator_function(origional_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper exectued this before {}'.format(origional_function.__name__))
        return origional_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print('display function ran')

# we dont need the two lines below if we add the syntax of @decorator_function
# decorated_display = decorator_function(display)


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Aaron', 34)

display()
