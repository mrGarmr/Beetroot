def binary_search_recursive(arr, target, left, right):
    # Базовий випадок: якщо left > right, елемент не знайдено
    if left > right:
        return -1
    
    # Знаходимо середину
    mid = (left + right) // 2
    
    # Якщо елемент у середині — це ціль, повертаємо його індекс
    if arr[mid] == target:
        return mid
    
    # Якщо ціль менша за середній елемент, шукаємо в лівій половині
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Якщо ціль більша, шукаємо в правій половині
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Тестування
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Елемент {target} знайдено за індексом: {result}")  # Очікуваний вивід: 3
    
    target = 8
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    print(f"Елемент {target} знайдено за індексом: {result}")  # Очікуваний вивід: -1