# message = "Hello, World!"
# print(message)
# Dunder __builtins__, __init__
message = "in Python, everything is an object."
print(message)
result = type(message)
print(result)

""" In Python, there are builtin tools:
(1) TYPES >> int, float, str, list, dict, set, tuple, bool
(2) FUNCTIONS >> print(), type(), len(), range(), input(), etc
(3) CONSTANTS >> True, False, None

"""
print(dir(__builtins__))
