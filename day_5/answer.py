import os


def main():
    ranges, ids = parse_input()
    combined_ranges = combine_ranges(ranges)
    total_ids = 0
    for crange in combined_ranges:
        total_ids += (crange[1] - crange[0]) + 1
    print("It added up to %s" % total_ids)
    #Part 1
    available = 0
    for pid in ids:
        for crange in combined_ranges:
            if pid >= crange[0] and pid <= crange[1]:
                available += 1
                break
        print("Finished checking %s, available is now %s" % (pid, available))


def combine_ranges(ranges):
    combined_ranges = []
    ranges = sorted(ranges, key=lambda x: x[0])
    combined_ranges = [ranges[0]]
    for range_ in ranges[1:]:
        if range_[0] <= combined_ranges[-1][1]:
            combined_ranges[-1][1] = max(combined_ranges[-1][1], range_[1])
        else:
            combined_ranges.append(range_)
    return combined_ranges


def parse_input():
    contents = read_input()
    ranges, ids = contents.split('\n\n')
    ranges = [[int(x) for x in range_.split('-')] for range_ in ranges.split('\n')]
    ids = [int(id_) for id_ in ids.split('\n')]
    return ranges, ids


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
