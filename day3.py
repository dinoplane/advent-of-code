import re
import sys

def read_input(filename):
    nums = []
    with open(filename, 'r') as file:
        data = file.read()

    return data

def part1(data):
    cmd = re.findall(r'mul\(([0-9]+)\,([0-9]+)\)', data)
    ret = 0
    for c in cmd:
        ret += int(c[0]) * int(c[1])
    return ret


def part2(data):
    return 0

def main():
    if len(sys.argv) != 2:
        print("Usage: python dayn.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = read_input(input_file)
    
    res1 = part1(nums)
    print("Part 1:", res1)

    res2 = part2(nums)
    print("Part 2:", res2)


if __name__ == '__main__':
    main()