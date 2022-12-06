def get_sides(foo):
    return list(map(int, foo.split()))

def main():
    input_file = open('day3input.txt')
    triangles = input_file.readlines()
    input_file.close()

    count = 0

    for triangle in triangles:
        sides = get_sides(triangle)
        sides.sort()

        if sides[0] + sides[1] > sides[2]:
            count += 1

    print("Part 1:", count)

    foo = list(map(get_sides, triangles))
    bar = [x[0] for x in foo] + [x[1] for x in foo] + [x[2] for x in foo]

    i = 0
    count2 = 0

    while i < len(bar):
        sides = [bar[i], bar[i+1], bar[i+2]]
        sides.sort()

        if sides[0] + sides[1] > sides[2]:
            count2 += 1

        i += 3

    print("Part 2:", count2)

if __name__ == '__main__':
    main()
