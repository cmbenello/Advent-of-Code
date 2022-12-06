with open('Advent of code 2021/day2/input.txt') as f:
    lines = f.readlines()


def part1(commands):
    x_pos = 0
    y_pos = 0

    for command in commands:
        move, d = command.split(" ")
        d = int(d)
        if move == "forward":
            x_pos += d
        elif move == "down":
            y_pos += d
        elif move == "up":
            y_pos -= d
    
    return(x_pos * y_pos)

def part2(commands):
    x_pos = 0
    y_pos = 0
    aim = 0

    for command in commands:
        move, d = command.split(" ")
        d = int(d)
        if move == "forward": 
            x_pos += d
            y_pos += aim * d
        elif move == "down":
            aim += d
        elif move == "up":
            aim -= d
    return(x_pos * y_pos)
    
print(part2(lines))