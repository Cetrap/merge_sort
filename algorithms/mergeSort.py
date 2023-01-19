import time
from settings import *


def merge(data, start, mid, end, draw_data, time_tick):
    p = start
    q = mid + 1
    temp_array = []

    for i in range(start, end + 1):
        if p > mid:
            temp_array.append(data[q])
            q += 1
        elif q > end:
            temp_array.append(data[p])
            p += 1
        elif data[p] < data[q]:
            temp_array.append(data[p])
            p += 1
        else:
            temp_array.append(data[q])
            q += 1

    for p in range(len(temp_array)):
        data[start] = temp_array[p]
        start += 1


def merge_sort(data, start, end, draw_data, time_tick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, draw_data, time_tick)
        merge_sort(data, mid + 1, end, draw_data, time_tick)

        merge(data, start, mid, end, draw_data, time_tick)

        draw_data(data, [RED if mid == x else WHITE for x in range(len(data))])
        time.sleep(time_tick)

    draw_data(data, [WHITE for x in range(len(data))])
