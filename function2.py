# Default Argument Values

# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# greeting1 = greet("Alice")
# print(greeting1)  # Output: Hello, Alice!

# return keyword 

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result1 = check_even_odd(10)
print(result1)  # Output: Even

result2 = check_even_odd(7)
print(result2)  # Output: Od