def compare_search_algorithms(arr, target):

    # -------------------- Linear Search --------------------
    linear_index = -1
    linear_comparisons = 0
    

    for i in range(len(arr)):
        linear_comparisons += 1

        if arr[i] == target:
            linear_index = i
            break

    # -------------------- Binary Search --------------------
    binary_index = -1
    binary_comparisons = 0

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        binary_comparisons += 1

        if arr[mid] == target:
            binary_index = mid

            # Continue searching on the left
            # to find the first occurrence.
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    # -------------------- Comparison Result --------------------
    if linear_comparisons < binary_comparisons:
        better = "Linear Search"
    elif binary_comparisons < linear_comparisons:
        better = "Binary Search"
    else:
        better = "Both Equal"

    # -------------------- Required Output --------------------
    result = [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {linear_index}",
        f"Comparisons: {linear_comparisons}",
        "Binary Search",
        f"Index: {binary_index}",
        f"Comparisons: {binary_comparisons}",
        f"Better Algorithm: {better}"
    ]

    return result