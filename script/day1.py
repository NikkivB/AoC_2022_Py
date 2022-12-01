
def part1():
    with open("../input/day1.txt", "r", encoding="utf-8") as input:
        input = input.readlines()
        input = [i.strip("\n") for i in input]

        calories = []
        temp = 0
        for i in input:
            if i == "":
                calories.append(temp)
                temp = 0
            else:
                temp += int(i)
        if temp > 0:
            calories.append(temp)
    return calories


def part2(calories):
    calories = sorted(calories, reverse=True)
    return sum(calories[:3])


if __name__ == "__main__":
    part1_answer = part1()
    print("day 1, part 1:", max(part1_answer))
    part2_answer = part2(part1_answer)
    print("day 1, part 2:", part2_answer)
