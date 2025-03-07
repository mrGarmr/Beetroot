# Прочитати про Fibonacci search та імплементуйте його за допомогою Python. Визначте складність алгоритму та порівняйте його з бінарним пошуком


def fibonacci_search(arr, target):
    def get_fibonacci_numbers(n):
        fib = [0, 1]
        while fib[-1] <= n:
            fib.append(fib[-1] + fib[-2])
        return fib
    
    n = len(arr)
    if n == 0:
        return -1
    
    # Отримуємо числа Фібоначчі
    fib = get_fibonacci_numbers(n)
    
    # Ініціалізуємо змінні
    offset = -1  # Зсув для відкинутих елементів
    k = len(fib) - 1  # Індекс найбільшого числа Фібоначчі
    
    while k > 1:
        # Обчислюємо індекс для порівняння
        i = min(offset + fib[k - 2], n - 1)
        
        # Якщо ціль знайдено
        if arr[i] == target:
            return i
        
        # Якщо ціль менша, шукаємо в лівій частині
        elif arr[i] > target:
            k -= 1
        
        # Якщо ціль більша, відкидаємо ліву частину
        else:
            offset = i
            k -= 2
    
    # Перевірка останнього елемента
    if k == 1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1

# Тестування
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = fibonacci_search(arr, target)
    print(f"Елемент {target} знайдено за індексом: {result}")  # Очікуваний вивід: 3
    
    target = 8
    result = fibonacci_search(arr, target)
    print(f"Елемент {target} знайдено за індексом: {result}")  # Очікуваний вивід: -1