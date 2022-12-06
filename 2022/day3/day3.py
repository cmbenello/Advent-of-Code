with open('2022/day3/input.txt') as f:
    lines = f.readlines()
    res = 0


    def helper(lists):
        for letter in lists[0]:
            if letter in lists[1] and letter in lists[2]:
                return letter

    counter = 0
    temp_list = []
    for line in lines:
        temp_list.append(line)
        if counter == 2:
            letter = helper(temp_list)
            if letter.isupper():
                res += 27 + ord(letter) - ord("A")
            else:
                res += 1 +ord(letter) - ord("a")
            temp_list = []
            counter = -1
        counter += 1
        
    print(res)