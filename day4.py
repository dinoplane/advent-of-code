import re
import sys

def read_input(filename):
    nums = []
    with open(filename, 'r') as file:
        data = file.readlines()
        data = [x.strip() for x in data]
    

    return data

def lookRight(data, x, y, width, height):
    if x+3 < width:
        return data[y][x:x+4] == 'XMAS'
    return False

def lookLeft(data, x, y, width, height):
    if x-3 > -2:
        return data[y][x-3:x+1] == 'SAMX'
    return False

def lookUp(data, x, y, width, height):
    if y-3 > -2:
        return data[y][x] == 'X' and data[y-1][x] == 'M' and data[y-2][x] == 'A' and data[y-3][x] == 'S'
    return False

def lookDown(data, x, y, width, height):
    if y+3 < height:
        return data[y][x] == 'X' and data[y+1][x] == 'M' and data[y+2][x] == 'A' and data[y+3][x] == 'S'
    return False

def lookUpRight(data, x, y, width, height):
    if (x+3 < width) and (y-3 > -2):
        return data[y][x] == 'X' and data[y-1][x+1] == 'M' and data[y-2][x+2] == 'A' and data[y-3][x+3] == 'S'
    return False

def lookUpLeft(data, x, y, width, height):
    if (x-3 > -2) and (y-3 > -2):
        return data[y][x] == 'X' and data[y-1][x-1] == 'M' and data[y-2][x-2] == 'A' and data[y-3][x-3] == 'S'
    return False

def lookDownRight(data, x, y, width, height):
    if (x+3 < width) and (y+3 < height):
        return data[y][x] == 'X' and data[y+1][x+1] == 'M' and data[y+2][x+2] == 'A' and data[y+3][x+3] == 'S'
    return False

def lookDownLeft(data, x, y, width, height):
    if (x-3 > -2) and (y+3 < height):
        return data[y][x] == 'X' and data[y+1][x-1] == 'M' and data[y+2][x-2] == 'A' and data[y+3][x-3] == 'S'
    return False

def part1(data):
    width = len(data[0])
    height = len(data)
    print(width, height)
    debmat = [[0 for i in range(width)] for j in range(height)]
    found = 0
    for j in range(height):
        for i in range(width):
            found += 1 if lookDown(data, i, j, width, height)  else 0
            found += 1 if lookUp(data, i, j, width, height) else 0
            found += 1 if lookRight(data, i, j, width, height)  else 0
            found += 1 if lookLeft(data, i, j, width, height)  else 0
            found += 1 if lookUpRight(data, i, j, width, height)  else 0
            found += 1 if lookUpLeft(data, i, j, width, height)  else 0
            found += 1 if lookDownRight(data, i, j, width, height)  else 0
            found += 1 if lookDownLeft(data, i, j, width, height) else 0
    # for j in range(height):
    #     for i in range(width):
    #         if debmat[j][i] == 1:
    #             print(data[j][i], end="")
    #         else:
    #             print(".", end="")
    #     print()

    return found
def part2(data):
    pass

    return 

def main():
    if len(sys.argv) != 2:
        print("Usage: python dayn.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = read_input(input_file)
    
    res1 = part1(nums)
    print("Part 1:", res1)

    # res2 = part2(nums)
    # print("Part 2:", res2)


if __name__ == '__main__':
    main()