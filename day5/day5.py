def get_seat_id(pass_data):
    row_num = to_base_10(pass_data[:7], 'F', 'B')
    seat_num = to_base_10(pass_data[7:], 'L', 'R')
    return row_num * 8 + seat_num


def to_base_10(num_str, zero, one):
    return int(num_str.replace(zero, '0').replace(one, '1'), 2)


def part1(data):
    return max(get_seat_id(pass_data) for pass_data in data)


def part2(data):
    seat_ids = list(sorted(get_seat_id(p) for p in data))
    for i, seat_id in enumerate(seat_ids):
        if (seat_ids[i + 1] == seat_id + 2):
            return seat_id + 1


if __name__ == '__main__':
    assert get_seat_id('BFFFBBFRRR') == 567
    assert get_seat_id('FFFBBBFRRR') == 119
    assert get_seat_id('BBFFBBFRLL') == 820

    with open('input.txt') as f:
        data = f.readlines()
    print('part1: ', part1(data))
    print('part2: ', part2(data))



