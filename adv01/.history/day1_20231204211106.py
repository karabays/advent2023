import re

digits = {"one": "1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

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
    # find_words = [d for d in digits if d in code]
    find_digits = [d for d in code if d.isdigit()]
    return {"code":code, 'decoded':decoded}

    


decoded_list = []

lines = read_input("input_small.txt")
for line in lines:
    decoded_list(find_words(line)