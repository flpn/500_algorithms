# Given an binary array, find maximum length sub-array having equal number of 0's and 1'.


# O(n^2)
def max_length_subarray(array):
    start = 0
    end = -1
    length = 0

    for i in range(len(array)):
        zeros = ones = 0

        for j in range(i, len(array)):
            if array[j] == 0:
                zeros += 1
            else:
                ones += 1

            if zeros == ones and j - i > length:
                start = i
                end = j
                length = j - i + 1

    print('Sub-array {}...{}, length {}'.format(start, end, length))


# O(n)
def max_length_subarray_two(array):
    dct = {0: -1}
    length = 0
    ending_index = -1
    total = 0

    for i in range(len(array)):
        total += -1 if array[i] == 0 else 1

        if total in dct.keys():
            if length < i - dct[total]:
                length = i - dct[total]
                ending_index = i
        else:
            dct[total] = i

    print('Sub-array {}...{}, length {}'.format(ending_index - length + 1, ending_index, length))


l = [0, 0, 1, 0, 1, 0, 0]
max_length_subarray(l)
max_length_subarray_two(l)
