import re
digits = {'one':"1",'two':"2",'three':"3",'four':"4",'five':"5",
           'six':"6",'seven':"7","eight":"8",'nine':"9"}

numerals = [1,2,3,4,5,6,7,8,9]


def decode(code):
    words = list(digits.keys())
    numbers = list(digits.values())
    keys = words + numbers
    code_dict = {}
    code_dict['decode'] = {}
    for k in keys:
        if k in code:
            locs = [m.start() for m in re.finditer(f'(?={k})', code)]

            code_dict["code"] = code
            for i in locs:
                code_dict['decode'][i] = k
    return code_dict

def load_file(file):
    with open (file) as input:
        calibration_doc = input.readlines()
    return calibration_doc

def convert_to_num (decoded):
    for k,v in decoded["decode"].items():
        if v in digits:
            decoded["decode"][k] = digits[v]
    return decoded

def find_min_max(code):
    mx = code['decode'][max(code['decode'])]
    mn = code['decode'][min(code['decode'])]
    return int(mn+mx)

def main():
    code_list = load_file('adv01/input.txt')
    codes = []
    for code in code_list:
        decoded = decode(code.strip())
        print(decoded)
        convert_to_num(decoded)
        min_max = find_min_max(decoded)
        codes.append(min_max)
    print(sum(codes))


main()