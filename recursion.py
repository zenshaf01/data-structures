"""
Recursion:
An algorithm which breaks down a problem to a smaller problem and calls itself to compute it.

One Branch:

Factorial:
Formula: n! = n * (n-1) * (n-2) * ... * 1
where n can be any positive integer

Or if we simplify the above equation:
n! = n * (n-1)! so,
5! = 5 * 4!.

Fibonacci:
Formula: F(n) = F(n-1) + F(n-2)
With base case being F(0) = 0 and F(1) = 1

Base case is the case where recursion should stop.
Recursive case is the case where recursion should continue.

While drawing, decision tree is beneficial to make sense of recursion
"""

# formula: n! = n * (n-1)!
# Time complexity: O(n)
# Memory complexity: O(n)
def factorial_recursive(n):
    if(n <= 1):
        return 1
    return n * factorial_recursive(n-1)

# formula: n! = n * (n-1)!
# Time complexity: O(n)
# Memory complexity: O(1)
def factorial_iterative(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

# Formula: f(n) = f(n-1) + f(n-2)
# Time complexity: O(2^n)
# Base case being F(0) = 0 and F(1) = 1
def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)