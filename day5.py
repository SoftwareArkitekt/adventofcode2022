def get_crates():
    # Get terrible input mess
    with open("day5_input.txt") as f:
        lines = f.readlines()
    lines = lines[0:9]
  
    # Rotate 90 degrees with zip
    rotated = list(zip(*lines[::-1]))

    crates = []
    # Actual input starts with a stack number
    for l in rotated:
        if l[0].isnumeric():
            crates.append(l)

    # Strip the stack numbers once we have the right rows
    for i in range(len(crates)):
        crates[i] = crates[i][1:]
    
    # Filter out all whitespaces
    for i in range(len(crates)):
        res = [i for i in crates[i] if i != ' ']
        crates[i] = res

    return crates

def part1():
    crates = get_crates()

    with open("day5_input_moves.txt") as f:
        lines = f.readlines()
    lines = lines[10:]

    for line in lines:
        print(line)
        moves = line.split()
        qty = int(moves[1])
        source = int(moves[3])
        dest = int(moves[5])

        for i in range(1, qty+1):
            crate = crates[source-1].pop()
            crates[dest-1].append(crate)
        
    print("Output:")
    for stack in crates:
        print(stack[-1:])

def part2():
    crates = get_crates()

    with open("day5_input.txt") as f:
        lines = f.readlines()
    lines = lines[10:]

    for line in lines:
        print(line)
        moves = line.split()
        qty = int(moves[1])
        source = int(moves[3])
        dest = int(moves[5])

        to_move = crates[source-1][-qty:]
        crates[source-1] = crates[source-1][:-qty]
        crates[dest-1].extend(to_move)

    print("Output:")
    for stack in crates:
        print(stack[-1:])
        
if __name__ == "__main__":
    part2()