with open('2022/day6/input.txt') as f:
    lines = f.readlines()

def part1(packets):
    res = 14
    packet = [char for char in packets[0][:14]]
    for char in packets[0][14:]:
        if len(set(packet)) == 14:
            return res
        packet.pop(0)
        packet.append(char)
        res += 1


print(part1(lines))