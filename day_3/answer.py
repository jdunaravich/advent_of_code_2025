import os


def main():
    banks = get_battery_banks()
    total_joltage = 0
    for battery in banks:
        print("Bank was %s" % battery)
        # max_joltage = get_max_joltage(battery=battery)
        max_joltage = get_max_joltage_2(battery=battery)
        print("Max Joltage was %s" % max_joltage)
        total_joltage += max_joltage
    print("Cumulative Joltage was %s" % total_joltage)

    # get_max_joltage(battery="987654321111111")
    # pass


def get_max_joltage(battery):
    for integer in range(9, 0, -1):
        left = str(integer)
        try:
            index_left = battery.index(left)
        except:
            continue
        if index_left == len(battery) - 1:
            continue
        right = max([int(num) for num in battery[index_left+1:]])
        max_joltage = "%s%s" % (battery[index_left], right)
        return int(max_joltage)


def get_max_joltage_2(battery):
    remaining = 11
    for integer in range(9, 0, -1):
        left = str(integer)
        try:
            index_left = battery[:-1*remaining].index(left)
        except:
            continue
        break
    joltage = [battery[index_left]]
    while remaining > 0:
        remaining -= 1
        search_space = battery[index_left+1:remaining * -1]
        if remaining == 0:
            search_space = battery[index_left+1:]
        highest = max(map(int, search_space))
        index_left += search_space.index(str(highest)) + 1
        joltage.append(str(highest))
    return int("".join(joltage))


def get_battery_banks():
    banks = read_input().split('\n')
    return banks


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
