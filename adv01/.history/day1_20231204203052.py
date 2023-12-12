
digits = {"one": "1", "two":"2", "three":"3", "four":4, "five":5, "six":6, "seven":"7", "eight":"8", "nine":"9"}

def read_input(file_name):
    with open(file_name) as f:
        data = f.readlines()
    raw_data = [d.split()[0] for d in data]
    return raw_data

def add_digits(code):
    finds = [d for d in digits if d in code]
    words = []
    for number in finds:
        idx = code.find(number)
        words.append({"number":number, "idx":idx})
    
    words_reversed = sorted(words, key=lambda x: x['number'], reverse=True)
    print(words)




lines = read_input("input_small.txt")
for line in lines:
    add_digits(line)