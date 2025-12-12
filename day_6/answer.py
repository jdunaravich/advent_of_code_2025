import os
from functools import reduce
import operator

def main():
    part_1()
    part_2()


def part_2():
    funcs = {
        '*': operator.mul,
        '+': operator.add
    }
    contents = read_input()
    # contents = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
    contents = contents.split("\n")
    operators = contents.pop().split()
    total = 0
    buffer = []
    for column in range(len(contents[0]) -1, -1, -1):
        numbers = [contents[row][column] for row in range(len(contents))]
        if all([number == ' ' for number in numbers]):
            # print("buffer was %s" % buffer)
            output = reduce(funcs[operators.pop()], buffer)
            # print("Output was %s" % output)
            total += output
            # print("Total is now %s" % total)
            buffer = []
            continue
        num_string = "".join(numbers).strip()
        buffer.append(int(num_string))
    output = reduce(funcs[operators.pop()], buffer)
    total += output
    print("Part 2 total was %s" % total)


def part_1():
    grid = get_grid()
    funcs = {
        '*': operator.mul,
        '+': operator.add
    }
    total = 0
    for col in range(len(grid[0])):
        output = reduce(funcs[grid[-1][col]], [int(grid[row][col]) for row in range(len(grid)-1)])
        total += output
    print("Part 1 total was %s" % total)


def get_grid():
    contents = read_input()
    contents = contents.split("\n")
    contents = [line.split() for line in contents]
    return contents


def read_input(input_file_name=None):
    if input_file_name is None:
        input_file_name = "input.txt"
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file_name = os.path.join(__location__, input_file_name)

    with open(input_file_name) as input_file:
        contents = input_file.read()
    return contents


if __name__ == '__main__':
    main()
