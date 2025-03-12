# Implement the mergeSort function without using the slice operator.

def merge(arr, left, mid, right):
    '''Implement the mergeSort'''
    n1 = mid - left + 1
    n2 = right - mid
    
    # Create temporary arrays
    L = [0] * n1
    R = [0] * n2
    
    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    # Merge the temporary arrays back into arr[left..right]
    i = j = 0  # Initial index of subarrays
    k = left  # Initial index of merged subarray
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        
        merge(arr, left, mid, right)

# Test 
def main():
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [8, 8],
        [],
        [0, 1, 1, -1, -1, 0],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    ]
    result_answears = [
        [11, 12, 22, 25, 34, 64, 90],
        [8, 8],
        [],
        [-1, -1, 0, 0, 1, 1],
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    ]

    for arr, result_arr in zip(test_cases, result_answears):
        print(f"Given list:    {arr}")
        mergeSort(arr, 0, len(arr) - 1)
        print(f"Sorted list:   {arr}\n")
        assert(arr==result_arr)

if __name__ == "__main__":
    main()