
def read_input(file_name):
    with open(file_name) as f:
        data = f.readlines()
    raw_data = [d.split()[0] for d in data]
    return raw_data

def add_digits()