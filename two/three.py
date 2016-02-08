import string
from edit_dis import edit_distance


def pprint(matrix):
    for row in matrix:
        for val in row:
            print '{:4}'.format(val),
        print

file_names = ['i', 'd', 's', 'r']
confusion = {}

for file_name in file_names:
    dis_list = []
    for index, line in enumerate(open(file_name)):
        if index != 0:
            dis_list.append([x.strip() for x in line.split('\t')[1:]])
    confusion[file_name] = dis_list


words = {}
words_count = 0.0
for line in open('variances'):
    l = line.split()
    words_count += int(l[2])
    words[l[0]] = int(l[2])


def spell(word):
    condidates = []
    for w in words.keys():
        ed, op = edit_distance(w, word)
        if ed >= 0 and ed <= 1:
            condidates.append((w, op))
    prob = []

    for cond, op in condidates:
        p_w = words[cond] / words_count
        for index, o in enumerate(op):
            if o != '-':
                if o == 's':
                    cost = confusion[o][
                        string.lowercase.index(word[index])
                    ][
                        string.lowercase.index(cond[index])
                    ]
                if o == 'd':
                    cost = confusion[o][
                        string.lowercase.index(word[index])
                    ][
                        string.lowercase.index(word[index])
                    ]
                if o == 'i':
                    cost = confusion[o][
                        string.lowercase.index(cond[index])
                    ][
                        string.lowercase.index(cond[index])
                    ]
        prob.append(p_w * int(cost))

    if not words.has_key(word):
        # for i in range(len(condidates)):
            # print condidates[i], prob[i]
        arg_max = prob.index(max(prob))
        return condidates[arg_max]
    else:
        return word
if __name__ == '__main__':
    print spell('thek')
    print spell('natura')
    print spell('natral')
