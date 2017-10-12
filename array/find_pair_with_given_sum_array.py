# Given an unsorted array of integers, find a pair with given sum in it


# O(n²)
def find_pair(array, total_sum):
    for i in range(len(array)):
        for j in range(0 + i, len(array)):
            if array[i] + array[j] == total_sum:
                print('Pair found at index {} and {}: ({} + {})'.format(i, j, array[i], array[j]))
                return

    print('Pair not found')


# O(n log n)
def find_pair_two(array, total_sum):
    array = sorted(array)
    low = 0
    high = len(array) - 1

    while low < high:
        if array[low] + array[high] == total_sum:
            print('Pair found at index {} and {}: ({} + {})'.format(low, high, array[low], array[high]))
            return
        elif (array[low] + array[high]) < total_sum:
            low += 1
        else:
            high -= 1

    print('Pair not found')


# O(n)
def find_pair_three(array, total_sum):
    dct = {}

    for i in range(len(array)):

        value = total_sum - array[i]

        if value in dct.keys():
            print('Pair found at index {} and {}: ({} + {})'.format(dct[value], i, array[dct[value]], array[i]))
            return

        dct[array[i]] = i

    print('Pair not found')


l = [8, 7, 2, 5, 3, 1]
total = 10

find_pair(l, total)
find_pair_two(l, total)
find_pair_three(l, total)
