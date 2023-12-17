import yaml

def convert_to_yaml():
    with open("adv05/input.txt") as f:
        txt = f.readlines()
    
    yaml_file = []
    for line in txt:
        if line[0].isdigit():
            yaml_file.append("- " + line)
        else:
            yaml_file.append(line)
    
    with open('adv05/input.yaml','w') as ff:
        ff.writelines(yaml_file)

def load_file(file):
    with open(file) as f:
        raw_file = yaml.safe_load(f)
    return raw_file

def parse_almanac(file):
    raw = load_file(file)
    almanac = {}
    almanac['seeds'] = [int(s) for s in raw['seeds'].split()]
    del raw['seeds']
    
    for map in raw:
        maps = []
        for entry in raw[map]:
            entry = entry.split()
            e = {'destination':int(entry[0]), 'source':int(entry[1]), 'range':int(entry[2])}
            maps.append(e)
        almanac[map.rstrip(" map")] = maps
    return almanac

def get_destination(seed, map):
    for m in map:
        if seed in range(m['source'], m['source']+m['range']):
            return seed - m['source'] + m['destination']

def this_to_that(these, those):
    result= []
    for this in these:
        that = get_destination(this, those)
        if that:
            result.append(get_destination(this, those))
        else:
            result.append(this)
    print(result)
    return result

def part1():
    file = 'adv05/input.yaml'
    almanac = parse_almanac(file)


    soils = this_to_that(almanac['seeds'], almanac['seed-to-soil'])
    print()
    fertilizers = this_to_that(soils,almanac['soil-to-fertilizer'])
    waters = this_to_that(fertilizers,almanac['fertilizer-to-water'])
    lights = this_to_that(waters,almanac['water-to-light'])
    temperatures = this_to_that(lights,almanac['light-to-temperature'])
    humidities = this_to_that(temperatures,almanac['temperature-to-humidity'])
    locations = this_to_that(humidities,almanac['humidity-to-location'])
    
    print(min(locations))


def part2():
    file = 'adv05/input.yaml'
    almanac = parse_almanac(file)

    seeds = []
    for i in range(0,len(almanac['seeds'])-1,2):
        seed_range = range(almanac['seeds'][i],almanac['seeds'][i]+almanac['seeds'][i+1])
        seeds.append(seed_range)

    print(seeds)
    for seed in seeds:
        print(seed)
        soils = this_to_that(seed, almanac['seed-to-soil'])
        print('worked soils...')
        fertilizers = this_to_that(soils,almanac['soil-to-fertilizer'])
        waters = this_to_that(fertilizers,almanac['fertilizer-to-water'])
        lights = this_to_that(waters,almanac['water-to-light'])
        temperatures = this_to_that(lights,almanac['light-to-temperature'])
        humidities = this_to_that(temperatures,almanac['temperature-to-humidity'])
        locations = this_to_that(humidities,almanac['humidity-to-location'])
        print("result....")
        print(min(locations))

#convert_to_yaml()
part2()