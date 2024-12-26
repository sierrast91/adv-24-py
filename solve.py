import sys
import importlib


def read_text(fn):
    fd = open(fn,"r")
    lines = []
    for line in fd.readlines():
        lines.append(line)
    return lines
def main():
    if len(sys.argv)<2:
        print("enter day to solve")
        return
    day = sys.argv[1]
    print(f"solving {day}")
    lines = read_text(f"day{day}.txt")
    day_m = importlib.import_module(f"day{day}")
    print("part1",day_m.solve1(lines))
    print("part2",day_m.solve2(lines))

if __name__ == "__main__" :
        main()
