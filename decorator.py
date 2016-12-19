# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             res = func(*args, **kw)
#             print('end')
#             return res
#         return wrapper
#     return decorator





@log  #now = log(now)
def now():
    print('2015-3-25')

now()
