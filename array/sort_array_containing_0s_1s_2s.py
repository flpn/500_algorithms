# Given an array containing only 0's, 1's and 2's, sort it in linear time and constant space.


# two traversal
def sort_array(array):
    zeros = ones = 0

    for i in array:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1

    for i in range(len(array)):
        if zeros > 0:
            array[i] = 0
            zeros -= 1
        elif ones > 0:
            array[i] = 1
            ones -= 1
        else:
            array[i] = 2


# one traversal
def sort_array_two(array):
    start = mid = 0
    end = len(array) - 1
    pivot = 1

    while mid <= end:
        if array[mid] < pivot:
            temp = array[start]
            array[start] = array[mid]
            array[mid] = temp

            start += 1
            mid += 1

        elif array[mid] > pivot:
            temp = array[mid]
            array[mid] = array[end]
            array[end] = temp

            end -= 1

        else:
            mid += 1


l = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]

sort_array(l)
sort_array_two(l)
print(l)
