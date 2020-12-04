import re
import functools


mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def parse(raw_data):
    data = raw_data.split('\n\n')
    data = [re.split(r'\s|\n', s) for s in data]
    return data


def count_valid(data):
    return functools.reduce(
        lambda acc, p: acc + 1 if is_valid(p) else acc,
        data, 0)


def is_valid(data):
    fields_list = [x.split(':')[0] for x in data]
    for field in mandatory_fields:
        if field not in fields_list:
            return False
    return True


if __name__ == '__main__':
    with open('test_input.txt') as f:
        test_data = parse(f.read())
    test_result = count_valid(test_data)
    print('test_result = ', test_result)
    assert test_result == 2
    
    with open('input.txt') as f:
        data = parse(f.read())
    result = count_valid(data)
    print('result = ', result)
