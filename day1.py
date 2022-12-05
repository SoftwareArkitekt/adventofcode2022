def main():
    elves = []
    current_sum = 0

    with open("day1_input.txt") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if len(line) > 0:
            current_sum += int(line)
        else:
            elves.append(current_sum)
            current_sum = 0
        
    elves.sort(reverse=True)
    top3 = elves[0:3]
    output = sum(top3)
    print("Top 3:")
    print(top3)
    print("Output:")
    print(output)

if __name__ == "__main__":
    main()