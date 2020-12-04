import re
import functools


class Passeport:

    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, fields_data):
        self.fields = []
        for field_data in fields_data:
            if not field_data:
                continue

            self.fields.append(
                Field(field_data))

    def validate(self):
        fields_name = [f.name for f in self.fields]
        for field in self.mandatory_fields:
            if field not in fields_name:
                return False
        for field in self.fields:
            if not field.validate():
                return False
        return True


class Field:
    def __init__(self, field_data):
        splited = field_data.split(':')
        self.name = splited[0]
        self.value = splited[1]

    def validate(self):
        if self.name == 'byr':
            return self.validate_year(1920, 2002)
        elif self.name == 'iyr':
            return self.validate_year(2010, 2020)
        elif self.name == 'eyr':
            return self.validate_year(2020, 2030)
        elif self.name == 'hgt':
            if re.match(r'\d+(cm)', self.value):
                num = int(self.value[:-2])
                return (num >= 150 and num <= 193)
            elif re.match(r'\d+(in)', self.value):
                num = int(self.value[:-2])
                return (num >= 59 and num <= 76)
            return False
        elif self.name == 'hcl':
            return re.match(r'^#(([a-f]|[0-9]){6})$', self.value)
        elif self.name == 'ecl':
            return self.value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif self.name == 'pid':
            return re.match(r'^[0-9]{9}$', self.value)

        return True

    def validate_year(self, minYear, maxYear):
        return (len(self.value) == 4
            and int(self.value) >= minYear
            and int(self.value) <= maxYear)


def parse(raw_data):
    data = raw_data.split('\n\n')
    data = [re.split(r'\s|\n', s) for s in data]
    return data


def count_valid(data):
    return functools.reduce(
        lambda acc, p: acc + 1 if Passeport(p).validate() else acc,
        data, 0)


if __name__ == '__main__':
    assert Field('byr:2002').validate()
    assert not Field('byr:2003').validate()
    assert Field('hgt:60in').validate()
    assert Field('hgt:190cm').validate()
    assert not Field('hgt:190in').validate()
    assert not Field('hgt:190').validate()
    assert Field('hcl:#123abc').validate()
    assert not Field('hcl:#123abz').validate()
    assert not Field('hcl:123abc').validate()
    assert Field('ecl:brn').validate()
    assert not Field('ecl:wat').validate()
    assert Field('pid:000000001').validate()
    assert not Field('pid:0123456789').validate()

    with open('test_input_valid.txt') as f:
        test_data_valid = parse(f.read())
    test_result_valid = count_valid(test_data_valid)
    print('test_result_valid = ', test_result_valid)
    assert test_result_valid == 4

    with open('test_input_invalid.txt') as f:
        test_data_invalid = parse(f.read())
    test_result_invalid = count_valid(test_data_invalid)
    print('test_result_invalid = ', test_result_invalid)
    assert test_result_invalid == 0
    
    with open('input.txt') as f:
        data = parse(f.read())
    result = count_valid(data)
    print('result = ', result)
