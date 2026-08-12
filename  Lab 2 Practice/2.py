arr = [5, 8, 2, 10, 7]
target = 10

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")