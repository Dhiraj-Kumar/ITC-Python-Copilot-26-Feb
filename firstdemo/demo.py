# Write a function to generate a fibonnaci sequence up to a given number n
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
n = 100
print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")