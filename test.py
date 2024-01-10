def merge(arr1, arr2, arr3):
    i = j = k = 0
    n = len(arr1)
    m = len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    # Copy the remaining elements of arr1
    while i < n:
        arr3[k] = arr1[i]
        i += 1
        k += 1

    # Copy the remaining elements of arr2
    while j < m:
        arr3[k] = arr2[j]
        j += 1
        k += 1

def print_array(ans):
    print(" ".join(map(str, ans)))

# Main function
def main():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6]
    arr3 = [0] * (len(arr1) + len(arr2))

    merge(arr1, arr2, arr3)
    print_array(arr3)

# Execute main function
if __name__ == "__main__":
    main()
