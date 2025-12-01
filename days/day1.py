from pkg_resources import resource_stream
from collections import Counter

turns = []
with resource_stream("input", "D1.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        n = int(line[1:])
        if line[0] == "R":
            turns.append(n)
        else:
            turns.append(-1 * n)


def part1():
    dialPosition=100050
    memo=0
    for turn in turns:
        dialPosition+=turn
        if dialPosition%100==0:
            memo+=1
    return memo
