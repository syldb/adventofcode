import re

def count_valid_pwd(data):
    total = 0
    for tup in data:
        valid = is_valid_part_2(tup[3], tup[0], tup[1], tup[2])
        if valid:
            total = total + 1
    return total


def is_valid_part_1(pwd, min_num, max_num, letter):
    counter = pwd.count(letter)
    return counter >= min_num and counter <= max_num

def is_valid_part_2(pwd, pos1, pos2, letter):
    return (pwd[pos1 - 1] == letter) ^ (pwd[pos2 - 1] == letter)

def str_to_tuple(data):
    for line in data:
        tup = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]*)", line).groups()
        yield (int(tup[0]), int(tup[1]), tup[2], tup[3])

if __name__ == '__main__':
    print('Start day2...')
    data = [
        (1, 3, 'a', 'abcde'),
        (1, 3, 'b', 'cdefg'),
        (2, 9, 'c', 'ccccccccc')
    ]
    result_test = count_valid_pwd(data)
    print('result test = ', result_test)
    assert result_test == 1
    with open('input2.txt') as f:
        raw_data = f.readlines()
    data = str_to_tuple(raw_data)
    result = count_valid_pwd(data)
    print('result = ', result)
    print('Exit day2.')
