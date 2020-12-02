def count_valid_pwd(data):
    total = 0
    for tup in data:
        valid = is_valid(tup[3], tup[0], tup[1], tup[2])
        if valid:
            total = total + 1
    return total


def is_valid(pwd, min_num, max_num, letter):
    counter = pwd.count(letter)
    return counter >= min_num and counter <= max_num


def str_to_tuple(data):
    for line in data:
        line_list = line.split(':')
        pwd = line_list[1].strip()
        line_list = line_list[0].split(' ')
        letter = line_list[1].strip()
        line_list = line_list[0].split('-')
        min_num = int(line_list[0])
        max_num = int(line_list[1])
        yield (min_num, max_num, letter, pwd)

if __name__ == '__main__':
    print('Start day2...')
    data = [
        (1, 3, 'a', 'abcde'),
        (1, 3, 'b', 'cdefg'),
        (2, 9, 'c', 'ccccccccc')
    ]
    result = count_valid_pwd(data)
    print('result test = ', result)
    assert result == 2
    with open('input2.txt') as f:
        raw_data = f.readlines()
    data = str_to_tuple(raw_data)
    result = count_valid_pwd(data)
    print('result = ', result)
    print('Exit day2.')
