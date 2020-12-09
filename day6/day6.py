def parse(raw_data):
    raw_data = raw_data.split('\n\n')
    for group in raw_data:
        group = group.splitlines()
        yield group


def part1(data):
    return sum([len(set(''.join(g))) for g in data])


def part2(data):
    # Not readable, but fun to write
    return sum([len(set.intersection(*[set(x) for x in group])) for group in data])


if __name__ == '__main__':
    with open('test_input.txt') as f:
        raw_data = f.read()
    data = parse(raw_data)
    # assert part1(data) == 11
    assert part2(data) == 6

    with open('input.txt') as f:
        raw_data = f.read()
    data = parse(raw_data)
    # print('part1: ', part1(data))
    print('part2: ', part2(data))
