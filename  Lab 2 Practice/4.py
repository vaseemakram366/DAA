# Insertion sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [5, 3, 4, 1, 2]

print("Before sorting:", arr)
print("After sorting:", insertion_sort(arr))

# Best Case:    O(n)
# Average Case: O(n²)
# Worst Case:   O(n²)
# Space:        O(1)