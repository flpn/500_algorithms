# Given two sorted arrays X and Y of size m and n each, merge the elements of X with elements of Y by maintaining the
# sorted order (fill X with the first m smallest elements and fill Y with remaining elements). This conversion should be
# done in-place and without using any other data structure.


# O(mn)
def merge(array_x, array_y):
    count = 0
    while count < len(array_x):
        if array_x[count] > array_y[0]:
            array_x[count], array_y[0] = array_y[0], array_x[count]

            for i in range(len(array_y) - 1):
                if array_y[i] > array_y[i + 1]:
                    array_y[i], array_y[i + 1] = array_y[i + 1], array_y[i]

        count += 1


x = [1, 4, 7, 8, 10]
y = [2, 3, 9]

merge(x, y)
print('X: {}\nY: {}'.format(x, y))
