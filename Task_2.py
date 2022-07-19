''' На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) 
отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком 
чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует 
заданным критериям. '''

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [j for j in array[1:] if j > pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

# Здесь представлена "Быстрая сортировка". При правильном выборе опорного элемента данный алгоритм
# является одним из самых быстрых (O(n log n)). Конечно, в работе разработчика чаще используется алгоритм
# Timsort, который входит в метод sort().
