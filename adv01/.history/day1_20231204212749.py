import re

digits = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
numbers = {'1','2','3','4','5','6','7','8','9'}

def read_input(file_name):
    with open(file_name) as f:
        data = f.readlines()
    raw_data = [d.split()[0] for d in data]
    return raw_data

def find_words(code):
    decoded = []
    for d in digits:
        idx = [match.start() for match in re.finditer(d, code)]
        if idx:
            for i in idx:
                decoded.append({i:d})
    return {"code":code, 'decoded':decoded}

def find_digits(code_dict):
    for n in numbers:
        idx = [match.start() for match in re.finditer(n, code_dict['code'])]
        if idx:
            for i in idx:
                code_dict['decoded'].append({i:n})
    return code_dict

def decode():
    decoded_list = []

    lines = read_input("input_small.txt")
    for line in lines:
        decoded_list.append(find_words(line))

    final_list = []
    for fline in decoded_list:
        final_list.append(find_digits(fline))

    return final_list

def find_code(code):
    first = code['decoded'].keys()
    last = [c for c in code['decoded']]
    print(code, first, last)

decoded_list = decode()

for code in decoded_list:
    find_code(code)
