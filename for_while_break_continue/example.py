# Условие задачи: дана двумерная матрица 3x3 (двумерный массив).
# Определить максимум и минимум каждой строки, а также их индексы.

matrix = [
    [9, 2, 1],
    [2, 5, 3],
    [4, 8, 5]
]

# Нам нужно найти минимумы в каждой строке и индексы этих минимумов (номера столбцов с минимальным элементом).

# Заведём списки, где мы будем хранить ответ на наш вопрос:
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
# Для начала напишем цикл, в котором пройдём по всем строкам матрицы
for row in matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]

    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)

print("Минимальные элементы:", min_value_rows)
print("Их индексы:", min_index_rows)
print("Максимальные элементы:", max_value_rows)
print("Их индексы:", max_index_rows)