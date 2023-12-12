
def load_file(file):
    with open(file) as f:
        raw_file = f.readlines()
    
    return [r.strip() for r in raw_file]

def parse_game(game):
    result = {}
    game = game.split(':')
    game_no = game[0]
    draws = game[1].split(";")
    result['game']=game_no
    result['draws'] = []
    for draw in draws:
        result['draws'].append(parse_draw(draw))
    return result

def parse_draw(draw):
    colors = draw.split(",")
    result = {}
    for color in colors:
        c = color.split()[1]
        n = color.split()[0]
        result[c] = int(n)
    return result

def test_result(game):
    condition = {'blue': 14, 'red': 12, 'green': 13}
    binary = []
    list_total = []
    for draw in game['draws']:
        blue = draw.get('blue',0)
        red = draw.get('red',0)
        green = draw.get('green',0)
        if blue <= condition['blue'] and red <= condition['red'] and green <= condition['green']:
            binary.append(True)
        else:
            binary.append(False)
    if all(binary):
        return int(game['game'].split()[1])
    

def part1(games_list):
    game_numbers = []
    for line in games_list:
        game = parse_game(line)
        if test_result(game):
            game_numbers.append(test_result(game))
    print(f'Part 1: {sum(game_numbers)}')

def find_min_set(game):
    blues = []
    reds = []
    greens = []
    for draw in game['draws']:
        blues.append(draw.get('blue',0))
        reds.append(draw.get('red',0))
        greens.append(draw.get('green',0))
    result = {"blue": max(blues),
            "red": max(reds),
            "green": max(greens)}

    return result['blue']*result['red']*result['green']

def part2(games_list):
    min_games = []
    for line in games_list:
        game = parse_game(line)
        min_set = find_min_set(game)
        min_games.append(min_set)
    print(min_games)
    print(sum(min_games))



def main():
    games_text = load_file("adv02/input.txt")
    part1(games_text)
    part2(games_text)
    


main()