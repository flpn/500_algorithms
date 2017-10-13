# Given an binary array, sort it in linear time and constant space. Output should print contain all zeroes followed
# by all ones.


def sort_binary_array(array):
    zeros = 0

    for i in array:
        if i == 0:
            zeros += 1

    for i in range(len(array)):
        if zeros > 0:
            array[i] = 0
            zeros -= 1
        else:
            array[i] = 1


l = [1, 0, 1, 0, 1, 0, 0, 1]

sort_binary_array(l)
print(l)
