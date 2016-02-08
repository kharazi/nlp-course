str_one = 'AGCACACA'
str_two = 'ACACACTA'


def pprint(matrix):
    for row in matrix:
        for val in row:
            print '{:4}'.format(val),
        print


def s(a, b):
    return 2 if a == b else -1


def locate_max(a):
    max_indicies = []
    largest = max(a)
    for index, element in enumerate(a):
        if largest == element:
            max_indicies.append(index)

    return largest, max_indicies


def edit_distance(first_str, second_str, w=-1):
    # Initialize distance matrix
    distance = [
        [0] * (len(second_str) + 1) for i in range(len(first_str) + 1)
    ]
    # Initialize ptr matrix
    ptr = [
        ['o'] * (len(second_str) + 1) for i in range(len(first_str) + 1)
    ]

    # Edit distance algorithm
    for i in range(1, len(first_str) + 1):
        for j in range(1, len(second_str) + 1):
            k = [distance[i - k][j] + w for k in range(1, i)]
            l = [distance[i][j - l] + w for l in range(1, j)]
            # print k, l
            if not k:
                k = [0]
            if not l:
                l = [0]
            values = (
                0,
                distance[i - 1][j - 1] + s(first_str[i - 1], second_str[j - 1]),
                max(k),
                max(l),
            )

            # print i, j, k, l, first_str[i - 1], second_str[j - 1]
            # print values
            distance[i][j], max_index = locate_max(values)
            # pprint(distance)
            # print min_index
            # max_index = values.index(max(values))
            op = ''
            if 1 in max_index:
                op += 'D'
            if 2 in max_index:
                op += 'T'
            if 3 in max_index:
                op += 'L'

            ptr[i][j] = op
            # pprint(distance)
            # print '-------'

    # print '-------\n' * 1
    pprint(distance)
    # print '-------\n' * 1

    pprint(ptr)
    row = len(ptr) - 1
    col = len(ptr[0]) -1
    stack = []
    while 1:
        # print row, col
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
            print "break"
            break
    pprint(ptr)

    print list(second_str)
    print stack[::-1]
    print list(first_str)
    # for row in range(len(ptr) - 1, 0, -1):
        # for col in range(len(ptr[0]) -1, 0, -1):
            # print row, col

edit_distance(str_one, str_two)
