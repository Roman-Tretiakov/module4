import time


def buble_sort(ls, is_timed=False):
    swapped = True
    start_time, end_time = None, None

    if is_timed:
        start_time = time.time()

    while swapped:
        swapped = False

        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapped = True

    if start_time is not None:
        end_time = time.time()
        return ls, f'Time taken: {round(end_time - start_time, 2)}'
    else:
        return ls


def selection_sort(ls, is_timed=False):
    start_time, end_time = None, None

    if is_timed:
        start_time = time.time()

    for i in range(0, len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                min_index = j
        ls[min_index], ls[i] = ls[i], ls[min_index]

    if start_time is not None:
        end_time = time.time()
        return ls, f'Time taken: {round(end_time - start_time, 2)}'
    else:
        return ls


def insertion_sort(ls, is_timed=False):
    start_time, end_time = None, None

    if is_timed:
        start_time = time.time()

    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key

    if start_time is not None:
        end_time = time.time()
        return ls, f'Time taken: {round(end_time - start_time, 2)}'
    else:
        return ls


def measure_time(func, _list):
    start_time = time.time()
    perform = func(_list)
    end_time = time.time()

    result = end_time - start_time

    return perform, f'Time taken: {round(result, 2)}'
