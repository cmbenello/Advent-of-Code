def create_stacks(lines):

    number_of_stacks = int(len(lines[0])/4)
    stacks = [[] for x in range(number_of_stacks)]

    for line in lines:
        for pos, i in enumerate(line):
            if i.isalpha():   
                stacks[int((pos - 1) / 4)].append(i)

        if line[1] == "1":
            stacks = [i[::-1] for i in stacks]
            return(stacks)

def part1():
    with open('2022/day5/input.txt') as f:
        lines = f.readlines()
        
        stacks = create_stacks(lines)

        for line in lines[10 :]:
            move_list = []
            l = line[:-1].split(" ")
            for i in l:
                if i.isnumeric():
                    move_list.append(int(i))
                    
            for i in range(move_list[0]):
                i = stacks[move_list[1] - 1].pop()
                stacks[move_list[2] - 1].append(i)
            
    
        res = []
        for stack in stacks:
            res.append(stack[-1])
        
        return("".join(res))

def part2():
    with open('2022/day5/input.txt') as f:
        lines = f.readlines()
        
        stacks = create_stacks(lines)

        for line in lines[10 :]:
            move_list = []
            l = line[:-1].split(" ")
            for i in l:
                if i.isnumeric():
                    move_list.append(int(i))
                    
            to_move = []
            for i in range(move_list[0]):
                to_move.append(stacks[move_list[1] - 1].pop())

            for move in to_move[::-1]:
                stacks[move_list[2] - 1].append(move)

    
        res = []
        for stack in stacks:
            res.append(stack[-1])
        
        return("".join(res))

print(part2())