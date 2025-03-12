# One way to improve the quicksort is to use an insertion sort on lists that are small in length (call it the "partition limit"). 
# Why does this make sense? Re-implement the quicksort and use it to sort a random list of integers. 
# Perform analysis using different list sizes for the partition limit.

import random
import time

def insertion_sort(arr, left, right):
    ''' Insertion Sort implemantation'''

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high, partition_limit):
    while low < high:
        if high - low + 1 < partition_limit:
            insertion_sort(arr, low, high)
            break
        else:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                quicksort(arr, low, pivot_index - 1, partition_limit)
                low = pivot_index + 1
            else:
                quicksort(arr, pivot_index + 1, high, partition_limit)
                high = pivot_index - 1

def quicksort_with_insertion(arr, partition_limit=10):
    quicksort(arr, 0, len(arr) - 1, partition_limit)

def analyze_sorting():
    sizes = [100, 1000, 5000, 10000]
    limits = [5, 10, 20, 50]
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nArray Size: {size}")
        for limit in limits:
            arr_copy = arr[:]
            start_time = time.time()
            quicksort_with_insertion(arr_copy, partition_limit=limit)
            end_time = time.time()
            print(f"Partition Limit {limit}: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    analyze_sorting()
