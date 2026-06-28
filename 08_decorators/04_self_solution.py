# import time

# def timer(func):
#       def wrapper(*args, **kwargs):
#          start = time.time()
#          result = func(*args, **kwargs)
#          end = time.time()
#          print(f'{func.__name__} ran in {end-start:.4f} seconds')
#          return result
#       return wrapper
        

# @timer
# def slow_function(n):
#      time.sleep(n)


# slow_function(3)

# print( "Finished executing slow_function.")
     


# Expected output:
# Calling add with (3, 5) {}
# add returned 8


def debug(func):
    def wrapper(*args, **kwargs):
         print(f"{func.__name__} with {args}  {kwargs}")
         result = func(*args, **kwargs)
         print(f"{func.__name__} returned {result}")
         return result
    return wrapper


 



@debug
def  add(a, b):
    return a + b

add(3, 5)
add(3, 10)
print("add(3, 5) returned", add(3, 5))

