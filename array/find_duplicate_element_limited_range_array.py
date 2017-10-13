# Given a limited range array of size n where array contains elements between 1 and n - 1 with one element repeating,
# find the duplicate number in it.


# O(n^2)
def find_duplicate(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return array[i]


# O(n) and O(n) auxiliary space
def find_duplicate_two(array):
    visited = [False for i in range(len(array) + 1)]

    for i in array:
        if visited[i]:
            return i

        visited[i] = True


# O(n) and O(n) auxiliary space
def find_duplicate_three(array):
    s = set()

    for i in array:
        if i not in s:
            s.add(i)
        else:
            return i


l = [1, 2, 3, 4, 4]
print('Number {} is repeated.'.format(find_duplicate(l)))
print('Number {} is repeated.'.format(find_duplicate_two(l)))
print('Number {} is repeated.'.format(find_duplicate_three(l)))
