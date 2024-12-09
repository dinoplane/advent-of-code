import re
import sys

import heapq

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
    leftlist = nums[0::2]
    rightlist = nums[1::2]
    
    heapq.heapify(leftlist)
    heapq.heapify(rightlist)
    
    sumDiffs = 0
    for i in range(len(nums) // 2):
        leftVal = heapq.heappop(leftlist)
        rightVal = heapq.heappop(rightlist)
        sumDiffs += abs(leftVal - rightVal)

    return sumDiffs


def part2(nums):
    leftlist = nums[0::2]
    rightlist = nums[1::2]
    
    countsInRight = {}
    for val in rightlist:
        countsInRight[val] = countsInRight.get(val, 0) + 1
    
    similarity = 0
    for val in leftlist:
        count = countsInRight.get(val, 0)
        similarity += val * count
    
    return similarity

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