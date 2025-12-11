import os
import time


def main():
    spins = get_spins_from_input()
    current_position = 50
    hit_zero = 0
    passed_zero = 0
    for direction, amount in spins:
        print("Current current_position is %s" % current_position)
        print("Spinning %s for %s clicks" % (direction, amount))
        if direction == 'L':
            if (current_position - amount) < 1:
                # new_passes = 1
                additional_passes = abs((current_position - amount) // 100)
                if ((current_position - amount) % 100) == 0:
                    additional_passes += 1
                if current_position == 0:
                    additional_passes -= 1
                # if additional_passes == 0:
                #     additional_passes = 1
                new_passes = additional_passes
                print("This caused 0 to be passed %s times" % new_passes)
                passed_zero += new_passes
            current_position = (current_position - amount) % 100
        elif direction == 'R':
            if (current_position + amount) > 99:
                new_passes = (current_position + amount) // 100
                print("This caused 0 to be passed %s times" % new_passes)
                passed_zero += new_passes
            current_position = (current_position + amount) % 100
        if current_position == 0:
            hit_zero += 1

        # if hit_zero != passed_zero:
        #     breakpoint()
        # time.sleep(1)
    print("Hit zero %s times" % hit_zero)
    print("Passed zero %s times" % passed_zero)


def get_spins_from_input(input_file_name=None):
    if input_file_name is None:
        input_file_name = "input.txt"
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file_name = os.path.join(__location__, input_file_name)

    with open(input_file_name) as input_file:
        contents = input_file.read()
    spins = []
    for line in contents.split('\n'):
        spins.append([line[0], int(line[1:])])
        # amount = int(line[1:])
        # spins.extend([[line[0], 1]] * amount)
    return spins


if __name__ == '__main__':
    main()
