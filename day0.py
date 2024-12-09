import re
import sys

def read_input(filename):
    nums = []
    with open(filename, 'r') as file:
        data = file.read()
        # print(data)
        nums = re.split(r'[ \n]+', data)
        # print(nums)
        nums = [int(num) for num in nums[:-1]]

    return nums

def part1(nums):
    return 0


def part2(nums):
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