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
        r = {}
        r['loc'] = (ast.start(), idx)
        result.append(r)
    return result 

def part2():
    lines = load_file('input.txt')
    grid = get_grid(lines)
    asterixes = []
    for idx, line in enumerate(lines):
        asterixes.extend(find_asterix(idx, line))
    print(asterixes)
part2()

