# Given an array of integers, print all subarrays having 0 sum.


# O(n^2)
def subarray_sum_0(array):
    for i in range(len(array)):
        total = 0

        for j in range(i, len(array)):
            total += array[j]

            if total == 0:
                print('Subarray: {}...{}'.format(i, j))


l = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
subarray_sum_0(l)
