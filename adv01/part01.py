

def find_codes(calibration_doc):
    calibration_num = []
    for line in calibration_doc:
        numbers = []
        for char in line:
            if char.isdigit():
                numbers.append(int(char))
        calibration_num.append(numbers)

    calibration_val = []
    for num in calibration_num:
        calibration_val.append(int(f"{num[0]}{num[-1]}"))
    print(sum(calibration_val))
    
if __name__ == "__main__":
    with open ('01/input.txt') as input:
        calibration_doc = input.readlines()
    find_codes(calibration_doc)