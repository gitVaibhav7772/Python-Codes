def fibonacci_sequence(n):
    result = []
    a, b = 0, 1

    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

fib = fibonacci_sequence(2000)
print(fib)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]


print("hi")
