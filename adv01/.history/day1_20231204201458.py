
digits = {"one": "1", "two":"2", "three":"3", "four":4, five, six, seven, eight, and nine}

def read_input(file_name):
    with open(file_name) as f:
        data = f.readlines()
    raw_data = [d.split()[0] for d in data]
    return raw_data

def add_digits(code):
    finds = [d for d in digits]