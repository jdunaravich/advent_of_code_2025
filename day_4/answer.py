import os


def main():
    # part_1()
    part_2()


def part_2():
    warehouse = get_map()
    total_accessible_rolls = 0
    iteration = 0
    while True:
        print("On iteration %s" % iteration)
        iteration += 1
        newly_accessed_rolls = count_and_remove_accessible_rolls(warehouse=warehouse)
        if newly_accessed_rolls:
            total_accessible_rolls += newly_accessed_rolls
        else:
            break
    print("In total %s rolls were accessible" % total_accessible_rolls)


def count_and_remove_accessible_rolls(warehouse):
    accessible_rolls = 0
    for row in range(len(warehouse)):
        for column in range(len(warehouse[0])):
            if not warehouse[row][column] == "@":
                continue
            rows = [row_ for row_ in [row - 1, row, row + 1] if row_ > -1 and row_ < len(warehouse)]
            cols = [col for col in [column - 1, column, column + 1] if col > -1 and col < len(warehouse[0])]
            total_rolls = 0
            for row_ in rows:
                for col_ in cols:
                    if row_ == row and col_ == column:
                        continue
                    if warehouse[row_][col_] == "@":
                        total_rolls += 1
            if total_rolls < 4:
                accessible_rolls += 1
                warehouse[row][column] = 'X'
    return accessible_rolls



def part_1():
    warehouse = get_map()
    accessible_rolls = 0
    for row in range(len(warehouse)):
        for column in range(len(warehouse[0])):
            if not warehouse[row][column] == "@":
                continue
            rows = [row_ for row_ in [row - 1, row, row + 1] if row_ > -1 and row_ < len(warehouse)]
            cols = [col for col in [column - 1, column, column + 1] if col > -1 and col < len(warehouse[0])]
            total_rolls = 0
            for row_ in rows:
                for col_ in cols:
                    if row_ == row and col_ == column:
                        continue
                    if warehouse[row_][col_] == "@":
                        total_rolls += 1
            if total_rolls < 4:
                accessible_rolls += 1
    print("%s rolls were accessible" % accessible_rolls)


def get_map():
    return [list(row) for row in read_input().split('\n')]


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
