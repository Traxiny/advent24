import re


def mul(x, y):
    return x * y

def calc_valid_muls(matches):
    result = 0
    calculate_mul = True
    for match in matches:
        if "do()" in match:
            calculate_mul = True
            continue
        elif "don't()" in match:
            calculate_mul = False
            continue
        
        if calculate_mul:
            result += mul(int(match[0]), int(match[1]))

    return result

if __name__ == "__main__":
    operation_result = 0
    with open("day3_input.txt", 'r') as f:
        input = f.read()
        regex = r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"
        operation_result = calc_valid_muls(re.findall(regex, input))
    print(operation_result)