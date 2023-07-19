def partition(a, low, high):
  """Partitions the list `a` around the pivot element."""
  pivot = a[high]
  i = low - 1
  for j in range(low, high):
    if a[j] <= pivot:
      i += 1
      a[i], a[j] = a[j], a[i]
  a[i + 1], a[high] = a[high], a[i + 1]
  return i + 1


def quick_sort(a, low, high):
  """Sorts the list `a` in ascending order using the quick sort algorithm."""
  if low < high:
    pivot = partition(a, low, high)
    quick_sort(a, low, pivot - 1)
    quick_sort(a, pivot + 1, high)


a = [10, 8, 2, 7, 3, 1, 9, 5, 6, 4]
quick_sort(a, 0, len(a) - 1)
print(a)