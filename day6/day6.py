def parse(raw_data):
    raw_data = raw_data.split('\n\n')
    for group in raw_data:
        group = group.splitlines()
        yield group


def part1(data):
    data = [len(set(''.join(g))) for g in data]
    return sum(data)


if __name__ == '__main__':
    with open('test_input.txt') as f:
        raw_data = f.read()
    data = parse(raw_data)
    assert part1(data) == 11

    with open('input.txt') as f:
        raw_data = f.read()
    data = parse(raw_data)
    print('part1: ', part1(data))
