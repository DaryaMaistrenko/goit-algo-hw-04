import timeit
import random

# 1. Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 2. Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3. Timsort (вбудований в Python)
def timsort(arr):
    return sorted(arr)

# Вимірювання часу виконання
def measure_sorting_times():
    data_sizes = [100, 1000, 10000, 100000]
    results = {}

    for size in data_sizes:
        random_data = [random.randint(0, 1000) for _ in range(size)]
        
        # Тестування сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(random_data.copy()), number=10)
        
        # Тестування сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(random_data.copy()), number=10)
        
        # Тестування Timsort
        timsort_time = timeit.timeit(lambda: timsort(random_data.copy()), number=10)
        
        results[size] = {
            'Merge Sort': merge_time,
            'Insertion Sort': insertion_time,
            'Timsort': timsort_time
        }

    # Вивід результатів
    for size, timing in results.items():
        print(f"Size: {size} -> Merge Sort: {timing['Merge Sort']:.5f}, Insertion Sort: {timing['Insertion Sort']:.5f}, Timsort: {timing['Timsort']:.5f}")

# Додаткове завдання: об'єднання k відсортованих списків
def merge_k_lists(lists):
    merged_list = []
    
    for lst in lists:
        merged_list.extend(lst)

    merge_sort(merged_list)
    return merged_list

# Приклад використання merge_k_lists
if __name__ == "__main__":
    print("Вимірювання часу виконання алгоритмів сортування:")
    measure_sorting_times()

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
