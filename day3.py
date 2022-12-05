def part1():
    with open("day2_input.txt") as f:
        lines = f.readlines()

    score = 0
    for line in lines:
        line = line.strip()
        print(line, " -> " ,ord(line[0]), ord(line[2]), " -> ", (ord(line[2])-88) - (ord(line[0])-65))
        game = (ord(line[2])-88) - (ord(line[0])-65)

        # Score our move
        if 'X' in line:
            score += 1
        elif 'Y' in line:
            score += 2
        elif 'Z' in line:
            score += 3

        # Score our win/loss
        if game == 1 or game == -2:
            score += 6
        elif game == 0:
            score += 3
        else:
            pass

    print("Output:")
    print(score)

def part2():
    with open("day2_input.txt") as f:
        lines = f.readlines()

    score = 0
    for line in lines:
        line = line.strip()

        # Score our move
        if 'X' in line: # loss
            if 'A' in line: # We play C
                score += 3
            elif 'B' in line:  # We play A
                score += 1
            elif 'C' in line:  # We play B
                score += 2
        elif 'Y' in line: # draw
            score += 3
            if 'A' in line: # We play A
                score += 1
            elif 'B' in line:  # We play B
                score += 2
            elif 'C' in line:  # We play C
                score += 3
        elif 'Z' in line: # win
            score += 6
            if 'A' in line: # We play B
                score += 2
            elif 'B' in line:  # We play C
                score += 3
            elif 'C' in line:  # We play A
                score += 1

    print("Output:")
    print(score)

if __name__ == "__main__":
    part2()