from pkg_resources import resource_stream

ranges: list[tuple[int, int]] = []
ingredients: list[int] = []
with resource_stream("input", "inputD5.txt") as textInput:
    breakLine = False
    for line in textInput.readlines():
        line = line.decode().strip()
        if line == "":
            breakLine = True
            continue
        if not breakLine:
            l, r = line.split("-")
            ranges.append((int(l), int(r)))
        else:
            ingredients.append(int(line))
ranges.sort(key=lambda t: t[0])


def part1():
    fresh = []
    for ingrendient in ingredients:
        for r in ranges:
            if ingrendient < r[0]:
                continue
            if ingrendient > r[1]:
                continue
            fresh.append(ingrendient)
            break
    return len(fresh)


def part2():
    pass
