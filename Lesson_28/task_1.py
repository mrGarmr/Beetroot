# A bubble sort can be modified to "bubble" in both directions. 
# The first pass moves "up" the list and the second pass moves "down." 
# This alternating pattern continues until no more passes are necessary. 
# Implement this variation and describe under what circumstances it might be appropriate.

def both_directional_bubble_sort(arr):
    '''Implementation of both directions bubble sort'''

    if len(arr) <= 1:
        return arr
    
    start = 0
    end = len(arr) - 1
    flag = True

    while flag:
        flag = False
        
        # Bubble up (left to right): Move largest element to the right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        
        if not flag:
            break
        
        # Move the right end, largest element in right place
        end -= 1
        flag = False
        
        # Bubble down (right to left): Move smallest element to the left
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
        
        # Move start, smallest element in right place
        start += 1
    
    return arr

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
        sorted_arr = both_directional_bubble_sort(arr)
        print(f"Sorted list:   {sorted_arr}\n")
        assert(sorted_arr==result_arr)

if __name__ == "__main__":
    main()