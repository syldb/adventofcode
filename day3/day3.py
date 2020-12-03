import itertools
import functools


def count_trees(data, right, down):
    total_trees = 0
    right_pos = 0
    for line in itertools.islice(data, None, None, down):
        str_line = str(line).strip()
        if str_line[right_pos] == '#':
            total_trees = total_trees + 1
        right_pos = (right_pos + right) % len(str_line)
    return total_trees


def count_trees_part_2(data, slope_list):
    return functools.reduce(
        lambda acc, slope: acc * count_trees(data, slope[0], slope[1]),
        slope_list,
        1
    )

if __name__ == '__main__':
    print('Start day 3...')
    with open('input3_test.txt') as f:
        test_data = f.readlines()
    test_result = count_trees(test_data, 3, 1)
    assert test_result == 7
    slope_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    test_result_2 = count_trees_part_2(test_data, slope_list)
    assert test_result_2 == 336
    with open('input3.txt') as f:
        data = f.readlines()
    result = count_trees(data, 3, 1)
    print('result = ', result)
    result_2 = count_trees_part_2(data, slope_list)
    print('result 2 = ', result_2)
    print('Exit day 3')
