def quick_sort(arr):
    if arr == []:
        return []

    pivot = arr[-1]   # choose last element as pivot
    list1 = []        # elements <= pivot
    list2 = []        # elements > pivot

    for item in arr[:-1]:
        if item > pivot:
            list2.append(item)
        else:
            list1.append(item)

    return quick_sort(list1) + [pivot] + quick_sort(list2)


inp = input("Enter the list numbers separated by a space: ").split()
arr = [int(x) for x in inp]

print("Unsorted list:", arr)
print("Sorted list is:", quick_sort(arr))
