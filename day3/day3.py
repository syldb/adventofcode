import itertools


def count_trees(data, right, down):
    total_trees = 0
    right_pos = 0
    for line in itertools.islice(data, None, None, down):
        str_line = str(line).strip()
        if str_line[right_pos] == '#':
            total_trees = total_trees + 1
        right_pos = (right_pos + right) % len(str_line)
    return total_trees


if __name__ == '__main__':
    print('Start day 3...')
    with open('input3_test.txt') as f:
        test_data = f.readlines()
    test_result = count_trees(test_data, 3, 1)
    print('test_result =', test_result)
    assert test_result == 7
    with open('input3.txt') as f:
        data = f.readlines()
    result = count_trees(data, 3, 1)
    print('result = ', result)
    print('Exit day 3')
