def bubble_sort(in_list):
    new_list = in_list.copy()
    length = len(new_list)

    while True:
        swaps = 0
        for i in range(1, length):
            if new_list[i] < new_list[i - 1]:
                (new_list[i], new_list[i - 1]) = (new_list[i - 1], new_list[i])
                swaps += 1
            if i == length - 1:
                length - 1
        if swaps == 0:
            break
    return new_list


def merge_sort(in_list):
    length = len(in_list)
    if length > 1:
        middle = length // 2
        left = in_list[:middle]
        right = in_list[middle:]
        merge_sort(left)
        merge_sort(right)
        ptr1 = 0
        ptr2 = 0
        for i in range(0, length):
            if ptr1 >= len(left) or ptr2 >= len(right):
                if ptr1 > ptr2:
                    value = right[ptr2]
                    ptr2 += 1
                else:
                    value = left[ptr1]
                    ptr1 += 1
                in_list[i] = value
            elif left[ptr1] <= right[ptr2]:
                in_list[i] = left[ptr1]
                ptr1 += 1
            else:
                in_list[i] = right[ptr2]
                ptr2 += 1


assert(bubble_sort([37, 42, 9, 19, 35, 4, 53, 22]) == [4, 9, 19, 22, 35, 37, 42, 53])
assert(bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5])
assert(bubble_sort([]) == [])

list1 = [37, 42, 9, 19, 35, 4, 53, 22]
merge_sort(list1)
assert(list1 == [4, 9, 19, 22, 35, 37, 42, 53])
