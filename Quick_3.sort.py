def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose the pivot element
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)


# Example usage
arr = [6, 2, 9, 1, 5, 8]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
