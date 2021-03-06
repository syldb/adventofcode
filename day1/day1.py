def find_result(report):
    for entry1 in report:
        for entry2 in report:
            for entry3 in report:
                total = int(entry1) + int(entry2) + int(entry3)
                if total == 2020:
                    return int(entry1) * int(entry2) * int(entry3)
    raise Exception('Entries not found')

if __name__ == '__main__':
    print('Day1 started')
    report = [1721, 979, 366, 299, 675, 1456]
    result = find_result(report)
    print('result example = ', result)
    assert result == 241861950

    with open('input1.txt') as f:
        report = f.readlines()
    result = find_result(report)
    print('result final = ', result)
