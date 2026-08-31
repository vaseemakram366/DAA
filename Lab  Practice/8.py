# Runtime and Complexity Comparison Table

# def generate_runtime_complexity_table(n):
# # your code goes here
# return []
import math
def generate_runtime_complexity_table(n):
    result = []
# output = []
result.append("Runtime Complexity Comparison")
result.append("Method ObservedCount ExpectedComplexityObservation")
linear_search = n
binary = math.floor(math.log2(m)) + 1 if m >= 1 else 0
# temp = n
# while temp > 0:
# binary_search += 1
# temp //= 2
bubble = n * (n - 1) // 2
insertion = n * (n - 1) // 2
result.append(f"Linear Search{linear_search} O(n) Grows linearly")
result.append(f"Binary Search{binary_search} O(log n) Grows logarithmically")
result.append(f"Bubble Sort{bubble_sort} O(n^2) Grows quadratically")
return resu
result.append(f"Insertion Sort{insertion_sort} O(n^2) Grows quadratically")