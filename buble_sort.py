def buble_sort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

lst = [3,4,8,1,9,3,6]
print(f'Исходный массив:{lst}')
result = buble_sort(lst)
print(f'Результат сортировки:{result}')
