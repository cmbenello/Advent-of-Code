with open('day1/input.txt') as f:
    lines = f.readlines()
    elfs = []
    sum = 0
    for i in lines:
        if i == '\n':
            elfs.append(sum)
            sum = 0
        else:
            sum += int(i)
    elfs.sort(reverse = True)
    print(elfs[0])
    print (elfs[0] + elfs[1] + elfs[2])
