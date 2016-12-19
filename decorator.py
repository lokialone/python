def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
            print('end')
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
