# Given an array of integers, find maximum length sub-array having given sum.


# O(n^2)
def max_length_subarray(array, total):
    start = 0
    end = 0
    length = 0

    for i in range(len(array)):
        s = 0

        for j in range(i, len(array)):
            s += array[j]

            if s == total and (j - i) > length:
                start = i
                end = j
                length = end - start + 1

    print('Subarray {}...{}, with length {}'.format(start, end, length))


# O(n)
def max_length_subarray_two(array, total):
    dct = {0: -1}
    total_sum = 0
    length = 0
    ending_index = -1

    for i in range(len(array)):
        total_sum += array[i]

        if total_sum not in dct.keys():
            dct[total_sum] = i

        if (total_sum - total) in dct.keys() and length < i - dct[total_sum - total]:
            length = i - dct[total_sum - total]
            ending_index = i

    print('Subarray {}...{}, with length {}'.format(ending_index - length + 1, ending_index, length))


l = [5, 6, -5, 5, 3, 5, 3, -2, 0]
s = 8

max_length_subarray(l, s)
max_length_subarray_two(l, s)
