def load_file(file):
    with open(file) as f:
        raw_file = f.readlines()
    return [r.strip() for r in raw_file]

def structure_data(line):
    result = {}
    card, numbers = line.split(':')
    w, t = numbers.split("|")
    winning = w.split()
    ticket = t.split()
    result['card'] = int(card.split()[1])
    result['winning'] = [int(a) for a in winning]
    result['ticket']  = [int(a) for a in ticket]
    result['count'] = 1
    #print(result)
    return result

def find_winning_numbers(card):
    winnigs = [ d for d in card['ticket'] if d in card['winning']]
    return winnigs

def part1():
    structured_data = []
    lines = load_file('adv04/input.txt')
    for line in lines:
        structured_data.append(structure_data(line))

    for card in structured_data:
        winnings = find_winning_numbers(card)
        if winnings:
            card['match'] = winnings

    result = []
    for c in structured_data:
        if 'match' in c:
            #print(c)
            result.append(2 ** (len(c['match'])-1) )

    print(sum(result))

def part2():
    #structured_data = [{"card":1, "win":3, 'count':1}, {"card":2, "win":2, 'count':1}, {"card":3, "win":1, 'count':1}, {"card":4, "win":0, 'count':1}, {"card":5, "win":1, 'count':1}]
    structured_data = []
    lines = load_file('adv04/input.txt')
    for line in lines:
        structured_data.append(structure_data(line))

    for card in structured_data:
        winnings = find_winning_numbers(card)
        card['win'] = len(winnings)

    for idx, card in enumerate(structured_data):
        for c in range(card['count']):
            for i in range(1,card['win']+1):
                if (idx+i) < len(structured_data):
                    structured_data[idx+i]['count'] += 1
    result = [c['count'] for c in structured_data]
    print(sum(result))
part2()