from pkg_resources import resource_stream

banks: list[str] = []
with resource_stream("input", "inputD3.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        banks.append(line)


def part1():
    memo = 0
    for bank in banks:
        volt = ""
        index1 = 0
        max_n = 0
        for i in range(len(bank) - 1):
            if bank[i] == "9":
                volt += bank[i]
                index1 = i
                break
            n = int(bank[i])
            if n > max_n:
                max_n = n
                index1 = i
        volt += str(max_n) if len(volt) != 1 else ""
        max_n = 0
        for i in range(index1 + 1, len(bank)):
            if bank[i] == "9":
                volt += bank[i]
                break
            n = int(bank[i])
            if n > max_n:
                max_n = n
        volt += str(max_n) if len(volt) != 2 else ""
        memo += int(volt)
    return memo


def part2():
    pass
