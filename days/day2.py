from pkg_resources import resource_stream

ranges: list[tuple[int, int]] = []
with resource_stream("input", "inputD2.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        for s in line.split(","):
            l, r = s.split("-")
            ranges.append((int(l), int(r)))


def part1():
    memo = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
            memo+=i if s1==s2 else 0
    return memo


def part2():
    pass
