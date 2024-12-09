import re
import sys

def read_input(filename):
    nums = []
    with open(filename, 'r') as file:
        data = file.read()
        # print(data)
        nums = re.split(r'[\n]+', data)
        # print(nums)
        nums = [re.split(' ', line) for line in nums]
        nums = [[int(num) for num in line] for line in nums]

    return nums

#  1 2 True = False
#  1 2 False = True
#  2 1 True = True
#  2 1 False = False

def isSafe(a, b, mustDecrease):
    if mustDecrease:
        return a > b and a - b > 0 and a - b < 4
    return a < b and b - a > 0 and b - a < 4
    # diff = a - b
    # return (0 < diff and diff < 4) if mustDecrease else (-4 < diff and diff < 0)

def checkLineSafetyP1(line):
    # print(line)
    mustDecrease = line[0] > line[1]
    for i in range(0, len(line)-1):
        # print(line[i], line[i+1], mustDecrease)
        if not isSafe(line[i], line[i+1], mustDecrease):
            return False
    return True
# 1 3 7 4 5

# 1 3 4 5
# 1 7 4 5

# 1 3 2 4 5
# 1 2 4 5
# 1 3 4 5

# 8 6 4 4 1

def checkLineSafetyP2(line, removedOne=False):
    # print(line)
    if line == []:
        return False
    
    mustDecrease = line[0] > line[1]
    
    for i in range(0, len(line)-1):
        if not isSafe(line[i], line[i+1], mustDecrease):
            if removedOne:
                return False
            else:
                # print("Removing", line[i], line[:i] + line[i+1:])
                # print("Removing", line[i+1], line[:i+1] + line[i+2:])
                # print("Removing", line[0], line[1:])
                
                if not (checkLineSafetyP2(line[:i] + line[i+1:], True) or checkLineSafetyP2(line[:i+1] + line[i+2:], True) or checkLineSafetyP2(line[1:], True)):
                    return False
                return True
    return True

def part1(nums):
    ret = 0
    for line in nums:
        if checkLineSafetyP1(line):
            ret += 1
    return ret

def part2(nums):
    ret = 0
    for line in nums:
        if checkLineSafetyP2(line):
            ret += 1
        else:
            pass
            # print("Not safe", line)
    return ret


def main():
    if len(sys.argv) != 2:
        print("Usage: python day1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = read_input(input_file)
    

    res1 = part1(nums)
    print("Part 1:", res1)

    res2 = part2(nums)
    print("Part 2:", res2)


if __name__ == '__main__':
    main()