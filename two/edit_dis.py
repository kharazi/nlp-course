str_one = 'execution'
str_two = 'intention'


def pprint(matrix):
    for row in matrix:
        for val in row:
            print '{:4}'.format(val),
        print

def locate_min(a):
    min_indicies = []
    smallest = min(a)
    for index, element in enumerate(a):
            if smallest == element: # check if this element is the minimum_value
                    min_indicies.append(index) # add the index to the list if it is

    return smallest, min_indicies

def edit_distance(first_str, second_str):
    # Initialize distance matrix
    distance = [
        [0] * (len(second_str) + 1) for i in range(len(first_str) + 1)
    ]
    for col in range(len(distance[0])):
        distance[0][col] = col
    for row in range(len(distance)):
        distance[row][0] = row

    # Initialize ptr matrix
    ptr = [
        ['o'] * (len(second_str) + 1) for i in range(len(first_str) + 1)
    ]

    # Edit distance algorithm
    for i in range(1, len(first_str) + 1):
        for j in range(1, len(second_str) + 1):
            values = (
                distance[i - 1][j] + 1,  # insert cost
                distance[i][j - 1] + 1,  # delete cost
                distance[i - 1][j - 1] + (2 if first_str[i - 1] != second_str[j - 1] else 0),
            )
            distance[i][j], min_index = locate_min(values)
            op = ''
            if 0 in min_index:
                op += 'T'
            if 1 in min_index:
                op += 'L'
            if 2 in min_index:
                op += 'D'

            ptr[i][j] = op


    row = len(ptr) - 1
    col = len(ptr[0]) -1
    stack = []
    while 1:
        if 'D' in ptr[row][col]:
            ptr[row][col] = ','
            row -= 1
            col -= 1
            if first_str[row] != second_str[col]:
                stack.append(
                    's'
                )
            else:
                stack.append(
                    '-'
                )
            continue
        if 'L' in ptr[row][col]:
            ptr[row][col] = ','
            col -= 1
            stack.append(
                'd'
            )

            continue
        if 'T' in ptr[row][col]:
            ptr[row][col] = ','
            row -= 1
            stack.append(
                'i'
            )

            continue
        if ptr[row][col] == 'o':
            # print "break"
            break
    return distance[-1][-1], stack[::-1]
