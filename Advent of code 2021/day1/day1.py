with open('Advent of code 2021/day1/input.txt') as f:
    lines = f.readlines()


def part1(depths):
    prev_depth = depths[0]
    count_inc = 0

    for depth in depths[1:]:
        if depth > prev_depth:
            count_inc += 1

        prev_depth = depth
    
    return count_inc


print(part1(lines ))