import os
from functools import reduce


def main():
    # is_invalid(111)
    # part_1()
    part_2()



def part_2():
    ranges = get_ranges()
    invalid = set()
    for beginning, end in ranges:
        for number in range(int(beginning), int(end) + 1):
            if is_invalid(number):
                invalid.add(number)
    answer = sum(invalid)
    print("All invalids added together were %s" % answer)


def is_invalid(number):
    num = str(number)
    # print("Number is %s" % num)
    for factor in factors(len(num)):
        # print("Factor is %s" % factor)
        foo = set([num[i:i + factor] for i in range(0, len(num), factor)])
        # print("That gives the following components: %s" % foo)
        if len(foo) == 1:
            # print("In this case, %s is invalid" % number)
            return True

def part_1():
    ranges = get_ranges()
    invalid = set()
    for beginning, end in ranges:
        for number in range(int(beginning), int(end) + 1):
            num = str(number)
            if len(num) % 2 == 0:
                if num[:len(num)//2] == num[len(num)//2:]:
                    invalid.add(num)
    print("All invalid added together is %s" % sum(map(int, invalid)))


def factors(n):
    """Returns all factors except for n of n"""
    if n == 1:
        return []
    factors = set(reduce(
        list.__add__,
        ([i, n // i] for i in range(1, int(n**0.5) + 1) if not n % i)))
    return sorted(factors)[:-1]


def get_ranges(input_file_name=None):
    if input_file_name is None:
        input_file_name = "input.txt"
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file_name = os.path.join(__location__, input_file_name)
    with open(input_file_name) as input_file:
        contents = input_file.read()
    ranges = [range_.split('-') for range_ in contents.split(",")]
    return ranges


if __name__ == '__main__':
    main()
