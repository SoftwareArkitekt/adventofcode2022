crates = [
    ['N','C','R','T','M','Z','P'],
    ['D','N','T','S','B','Z'],
    ['M','H','Q','R','F','C','T','G'],
    ['G','R','Z'],
    ['Z','N','R','H'],
    ['F','H','S','W','P','Z','L','D'],
    ['W','D','Z','R','C','G','M'],
    ['S','J','F','L','H','W','Z','Q'],
    ['S','Q','P','W','N']
]

def part1():
    with open("day5_input_moves.txt") as f:
        lines = f.readlines()

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
    print(crates)

def part2():
    with open("day5_input_moves.txt") as f:
        lines = f.readlines()

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
    print(crates)
        
if __name__ == "__main__":
    part2()