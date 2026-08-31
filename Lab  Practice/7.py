# Q1. 1.4 Algorithm Execution Observation Table

def generate_execution_observation_table(sizes):
# # your code goes here
# return []
# import math
# def recursive_fibonacci_count(n):
 if n <= 1:
 return 1
 return 1 + recursive_fibonacci_count(n - 1)+recursive_fibonacci_count(n - 2)
def generate_execution_observation_table(sizes):
 result = []
 result.append("algorithm Execution observation table")
 result.append("InputSize RecursiveFactorial IterativeFactorial" "RecursiveFibonacci
IterativeFibonacci LinearSearch" "BinarySearch BubbleSort InservationSort")
 for n in sizes:
 recursive_factorial = n + 1
 iterative_factorial = n
 recursive_fibonacci = recursive_fibonacci_count(n)
 iterative_fibonacci = n
 linear_search = n
 binary_search = 0
 temp = n
 while temp > 0:
 binary_search += 1
 temp //= 2
 bubble_sort = n * (n - 1) // 2
 insertion_sort = n * (n - 1) // 2
 row = [
 n,
 recursive_factorial,
 iterative_factorial,
 recursive_fibonacci,
 iterative_fibonacci,
 linear_search,
 binary_search,
 bubble_sort,
 insertion_sort

 ]
 result.append("".join(map(str, row)))
 return "\n".join(result)
