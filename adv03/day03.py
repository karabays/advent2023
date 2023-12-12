import re

def load_file(file):
    with open(file) as f:
        raw_file = f.readlines()
    
    return [r.strip() for r in raw_file]