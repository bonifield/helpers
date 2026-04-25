import json
import time
import warnings



########################################################
####### example without decorators to show logic #######

def plain_decorator(func):
	def wrapper():
		print(f"calling: {func.__name__}")
		print("this is happening before the decorated function")
		func()
		print("this is happening after the decorated function")
		print(f"done: {func.__name__}")
	return wrapper

def hi():
	print("Hi, all!")

decorated_hi = plain_decorator(hi)
decorated_hi()

# expected output
'''
calling: hi
this is happening before the decorated function
Hi, all!
this is happening after the decorated function
done: hi
'''



###########################################
####### decorator without arguments #######
print()

def fancy_decorator(func):
	def wrapper():
		print(f"calling: {func.__name__}")
		func()
		print(f"done: {func.__name__}")
	return wrapper

@fancy_decorator
def hello():
	print(f"Hello, world!")

hello()

# expected output
'''
calling: hello
Hello, world!
done: hello
'''



########################################
####### decorator with arguments #######
print()

def fancy_decorator2(func):
	def wrapper(*args, **kwargs):
		print(f"calling: {func.__name__}")
		out = func(*args, **kwargs)
		print(f"done: {func.__name__}")
		return out
	return wrapper

@fancy_decorator2
def hello2(fname, lname):
	print(f"Hello, {fname.title()} {lname.title()}!")

hello2("bob", "smith")

# expected output
'''
calling: hello2
Hello, Bob Smith!
done: hello2
'''



#################################
####### exception handler #######
print()

def catch_exceptions(func):
	def wrapper(*args, **kwargs):
		try:
			print(f"calling: {func.__name__}")
			return func(*args, **kwargs)
		except Exception as e:
			print(f"Error in {func.__name__}: {e}")
			return None
	return wrapper

@catch_exceptions
def div_by_zero(a, b):
	return a / b

div_by_zero(10, 0)

# expected output
'''
calling: div_by_zero
Error in div_by_zero: division by zero
'''



##########################################
####### role authenticator example #######
print()

# please do not do this in any production environments
example_user_permissions = {"username":"bob", "role":"user"}

def require_administrator(func):
	def wrapper(*args, **kwargs):
		print(f"calling: {func.__name__}")
		if example_user_permissions.get("role") != "admin":
			print("permission denied")
			return None
		return func(*args, **kwargs)
	return wrapper

@require_administrator
def delete_everything():
	print("deleted everything on all disks")

delete_everything()

# expected output
'''
calling: delete_everything
permission denied
'''



#############################################
####### add delay to network requests #######
print()

def delay(seconds):
	def decorator(func):
		def wrapper(*args, **kwargs):
			print(f"waiting {seconds}s before calling {func.__name__}")
			time.sleep(seconds)
			return func(*args, **kwargs)
		return wrapper
	return decorator

@delay(0.1)
def some_request():
	print("fetched data")

def call_many_requests():
	some_request()
	some_request()
	some_request()

call_many_requests()

# expected output
'''
waiting 0.1s before calling some_request
fetched data
waiting 0.1s before calling some_request
fetched data
waiting 0.1s before calling some_request
fetched data
'''



###################################
####### example cache check #######
print()

def simple_cache(func):
	cache = {}
	def wrapper(*args):
		if args in cache:
			print(f"args already in cache: {args}")
			return cache[args]
		result = func(*args)
		cache[args] = result
		return result
	return wrapper

@simple_cache
def heavy_math(n):
	return n * n * n

# does math the first time
print(heavy_math(5))
# returns from cache if arguments already used
print(heavy_math(5))

# expected output
'''
125
args already in cache: (5,)
125
'''



##########################################
####### network connection retries #######
print()

def retry(times):
	def decorator(func):
		def wrapper(*args, **kwargs):
			for i in range(times):
				try:
					return func(*args, **kwargs)
				except Exception as e:
					print(f"Attempt {i+1} failed. Retrying...")
					time.sleep(0.10)
			# last attempt without re-trying!
			return func(*args, **kwargs)
		return wrapper
	return decorator

@retry(times=3)
def unstable_network_call():
	import random
	if random.random() < 0.7:
		raise ConnectionError("Server is down!")
	return "Success!"

# commented because the exception ends the demo script
#print(unstable_network_call())
print("retry example commented out because exceptions terminate the demo script")

# expected output
'''
Attempt 1 failed. Retrying...
Attempt 2 failed. Retrying...
Attempt 3 failed. Retrying...
Success!
# or on failure
Traceback (most recent call last):
...
ConnectionError: Server is down!
'''



#####################################
####### JSON output formatter #######
print()

def as_json(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		return json.dumps({"status": "success", "data": result})
	return wrapper

@as_json
def get_user_data():
	return {"id": 1, "name": "Alice", "email": "alice@local"}

g = get_user_data()
print(type(g))
print(g)

# expected output
'''
<class 'str'>
{"status": "success", "data": {"id": 1, "name": "Alice", "email": "alice@local"}}
'''



###################################
####### deprecation warning #######
print()

def deprecated(func):
	def wrapper(*args, **kwargs):
		warnings.warn(f"{func.__name__} is deprecated and will be removed in a future release.", DeprecationWarning)
		return func(*args, **kwargs)
	return wrapper

@deprecated
def old_calculate_tax(price):
	return price * 0.05

print(old_calculate_tax(100))

# expected output
'''
python-decorators.py:290: DeprecationWarning: old_calculate_tax is deprecated and will be removed in a future release.
  warnings.warn(f"{func.__name__} is deprecated and will be removed in a future release.", DeprecationWarning)
5.0
'''



#################################################
####### debugging without functools.wraps #######
print()

def basic_unwrapped_decorator(func):
	def wrapper(*args, **kwargs):
		"""I am the wrapper docstring."""
		return func(*args, **kwargs)
	return wrapper

@basic_unwrapped_decorator
def say_hello():
	"""I am the original docstring."""
	print("Hello!")

print(say_hello.__name__)
print(say_hello.__doc__)

# expected output
'''
wrapper
I am the wrapper docstring.
'''



##############################################
####### debugging with functools.wraps #######
print()

from functools import wraps

# this is a good template for future use
def better_wrapped_decorator(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		"""I am the wrapper docstring."""
		out = func(*args, **kwargs)
		return out
	return wrapper

@better_wrapped_decorator
def say_hello():
	"""I am the original docstring."""
	print("Hello!")

print(say_hello.__name__)
print(say_hello.__doc__)

# expected output
'''
say_hello
I am the original docstring.
'''



#####################
####### words #######
print()

# stuff

# expected output
'''
'''
