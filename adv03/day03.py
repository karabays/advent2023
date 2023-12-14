import re

def load_file(file):
    with open(file) as f:
        raw_file = f.readlines()
    return [r.strip() for r in raw_file]

def find_numbers(idx, line):
    numbers = [m for m in re.finditer('\d+', line)]
    result = []
    for number in numbers:
        r = {}
        r['start'] = (number.start(), idx)
        r['end'] = (number.end(), idx)
        r['number'] = int(number.group())
        result.append(r)
    return result

def get_neighbours(number):
        space = []
        for i in range(number['start'][0], number['end'][0]):
            space.append((i,number['start'][1]))
        top_left = (max(number['start'][0]-1,0),max(number['start'][1]-1,0))
        bottom_right = (min(number['end'][0],139),min(number['end'][1]+1,139))
        neighbours = []
        for x in range(top_left[0],bottom_right[0]+1):
            for y in range(top_left[1], bottom_right[1]+1):
                if (x,y) not in space:
                    neighbours.append((x,y))
        #print(number, neighbours)
        return neighbours

def get_space(number):
    space = []
    for i in range(number['start'][0], number['end'][0]):
            space.append((i,number['start'][1]))
    return space

def get_grid(lines):
    grid = {}
    for idy, line in enumerate(lines):
        for idx, char in enumerate(line):
            grid[(idx,idy)] = char
    return grid


def part1():
    lines = load_file('input.txt')
    grid = get_grid(lines)
    numbers = []
    for idx, line in enumerate(lines):
        numbers.extend(find_numbers(idx, line))

    codes = []
    for number in numbers:
        neighbours = get_neighbours(number)
        for n in neighbours:
            if grid[n] != '.':
                #print(number['number'],n, neighbours)
                codes.append(number['number'])
    #result = list(dict.fromkeys(codes))

    print(sum(codes))

def find_asterix(idx, line):
    asterixes = [m for m in re.finditer('\*', line)]
    result = []
    for ast in asterixes:
        x = ast.start()
        y = idx
        r = {}
        r['ast'] = (x, y)
        r['neighbours'] = [(x-1,y-1),(x,y-1),(x+1,y-1),
                           (x-1,y),(x+1,y),
                           (x-1,y+1),(x,y+1),(x+1,y+1)]
        result.append(r)
    return result

def part2():
    lines = load_file('adv03/input.txt')
    grid = get_grid(lines)
    asterixes = []
    for idx, line in enumerate(lines):
        asterixes.extend(find_asterix(idx, line))


    numbers = []
    for idx, line in enumerate(lines):
        numb = find_numbers(idx, line)
        numbers.extend(numb)

    for n in numbers:
        n['space'] = get_space(n)


    addresses = {}
    for m in numbers:
        for s in m['space']:
            addresses[s] = m['number']

    #print(addresses)

    ratios = []
    for ast in asterixes:
            numbers_found = set([addresses.get(n) for n in ast['neighbours']])
            ratio = [q for q in numbers_found if q]
            if len(ratio) > 1:
                ratios.append(ratio)
    
    result = [r[0] * r [1] for r in ratios]
    print(sum(result))

part2()

