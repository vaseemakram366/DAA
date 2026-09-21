def compare_search_algorithms(arr, target):
    # your code goes here
  linear_index = -1
  linear_comparisons = 0

  for i in range(len(arr)):
    linear_comparisons += 1

    if arr[i] == target:
      lenear_index = id
      break

  binary_index = -1
  binary_comparisons = 0

  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    binary_comparisons += 1

    if arr[mid] == target:
      binary_index = mid
      right = mid - 1
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  if linear_comparisons < binary_comparisons:
    better = "Linear Search"
  elif binary_comparisons < linear_comparisons:
    better = "Binary Search"
  else:
    better = "Both Equal"
  return [
    "Search Comparison Report",
    "Linear Search",
    f"Index: {binary_index}",
    f"Comparisons: {linear_comparisons}",
    "Binary Search",
    f"Index: {binary_index}",
    f"Comparisons: {binary_comparisons}",
    f"Better Algorithm: {better}"
  ]
