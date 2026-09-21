def compare_merge_quick_task(tasks):
    def normalize(t):
        if isinstance(t, (tuple, list)):
            return (str(t[0]), int(t[1]))
        parts = t.split()
        return (parts[0], int(parts[1]))

    items = [normalize(t) for t in tasks]

    def before(a, b):
        if a[1] != b[1]:
            return a[1] > b[1]
        return a[0] < b[0]

    merge_count = 0

    def merge_sort(arr):
        nonlocal merge_count

        if len(arr) <= 1:
            return arr[:]

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        merged, i, j = [], 0, 0

        while i < len(left) and j < len(right):
            merge_count += 1

            if before(left[i], right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    merge_result = merge_sort(items)

    quick_count = 0

    def quick_sort(arr, low, high):
        nonlocal quick_count

        if low < high:
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                quick_count += 1

                if before(arr[j], pivot):
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]

            pi = i + 1
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    quick_arr = items[:]
    quick_sort(quick_arr, 0, len(quick_arr) - 1)

    lines = ["Task Prioritization Report", "Merge Sort Result"]
    lines += [f"{tid} {pr}" for tid, pr in merge_result]
    lines.append(f"Merge Comparisons: {merge_count}")

    lines.append("Quick Sort Result")
    lines += [f"{tid} {pr}" for tid, pr in quick_arr]
    lines.append(f"Quick Comparisons: {quick_count}")

    if merge_count < quick_count:
        better = "Merge Sort"
    elif quick_count < merge_count:
        better = "Quick Sort"
    else:
        better = "Both Equal"

    lines.append(f"Better Algorithm: {better}")

    return lines