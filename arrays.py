from sortfunc.sort_func import *

data_1 = [9, 7, 4, 5, 6, 7, 1, 2]
data_2 = [9, 7, 4, 5, 6, 7, 1, 2, 10, 1]
data_3 = [9, 7, 4, 5, 6, 7, 1, 2, 1, 2, 3]


print(measure_time(insertion_sort, data_1))
# print(insertion_sort(data_1, True))
# print(insertion_sort(data_2, True))
# print(insertion_sort(data_3, True))
#
# print(buble_sort(data_1, True))
# print(buble_sort(data_2, True))
# print(buble_sort(data_3, True))
#
# print(selection_sort(data_1, True))
# print(selection_sort(data_2, True))
# print(selection_sort(data_3, True))