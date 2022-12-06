def part1():
    with open('2022/day4/input.txt') as f:
        lines = f.readlines()
        res = 0

        for line in lines:
            x = [[int(j) for j in i.split("-")] for i in line[:-1].split(",")]
            if(x[0][0]<=x[1][0]and x[0][1]>=x[1][1]) \
                or (x[1][0]<=x[0][0]and x[1][1]>=x[0][1]):
                res += 1

        return(res)

def part2():
    with open('2022/day4/input.txt') as f:
        lines = f.readlines()
        res = 0

        for line in lines:
            x = [[int(j) for j in i.split("-")] for i in line[:-1].split(",")]
            if (x[1][0] <= x[0][0] <= x[1][1]) \
            or (x[0][0] <= x[1][0] <= x[0][1]):
                res += 1
        return res
print(part2())