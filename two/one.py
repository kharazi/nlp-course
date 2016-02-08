str_one = 'execution'
str_two = 'intention'

# str_one = 'inte'
# str_two = 'icef'

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
    # pprint(distance)
    # print '-------'

    # Initialize ptr matrix
    ptr = [
        ['o'] * (len(second_str) + 1) for i in range(len(first_str) + 1)
    ]

    # Edit distance algorithm
    for i in range(1, len(first_str) + 1):
        for j in range(1, len(second_str) + 1):
            # print i, j,(
                # distance[i - 1][j] + 1,
                # distance[i][j - 1] + 1,
                # distance[i - 1][j-1] + (2 if first_str[i - 1] != second_str[j - 1] else 0)
            # ), first_str[i - 1], second_str[j - 1]
            values = (
                distance[i - 1][j] + 1,  # insert cost
                distance[i][j - 1] + 1,  # delete cost
                distance[i - 1][j - 1] + (2 if first_str[i - 1] != second_str[j - 1] else 0),
            )
            distance[i][j], min_index = locate_min(values)
            # print min_index
            # min_index = values.index(min(values))
            op = ''
            if 0 in min_index:
                op += 'T'
            if 1 in min_index:
                op += 'L'
            if 2 in min_index:
                op += 'D'

            ptr[i][j] = op
            # pprint(distance)
            # print '-------'

    # pprint(distance)
    # print '-------\n' * 1

    pprint(distance)
    print '-------\n' * 1

    pprint(ptr)
    print '-------\n' * 1
    row = len(ptr) - 1
    col = len(ptr[0]) -1
    stack = []
    while 1:
    #     print row, col
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
    pprint(ptr)
    print '-------\n' * 1

    print list(second_str)
    print stack[::-1]
    print list(first_str)
    return distance[-1][-1], stack[::-1]
    # for row in range(len(ptr) - 1, 0, -1):
        # for col in range(len(ptr[0]) -1, 0, -1):
            # print row, col

print edit_distance(str_one, str_two)
