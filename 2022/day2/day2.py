with open('day2/input.txt') as f:
    lines = f.readlines()
    res = 0

    for line in lines:
        # A = Rock, # B = Paper, # C = Scissors
        temp = line.split(" ")
        left, right = temp[0][0], temp[1][0]

        curr = 0
        if right == "X": # lose
            if left == "A": # C
                curr += 3
            if left == "B": # A
                curr += 1
            if left == "C": # B
                curr += 2
        if right == "Y": # Draw
            curr += 3
            if left == "A": # A
                curr += 1
            if left == "B": # B
                curr += 2
            if left == "C": # C
                curr += 3
        if right == "Z": # Win
            curr += 6
            if left == "A": # B
                curr += 2
            if left == "B": # C
                curr += 3
            if left == "C": # A
                curr += 1

        res += curr
    print(res)