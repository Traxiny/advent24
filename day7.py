
from itertools import product

def create_operator_combinations(operands_cnt):
    operators = ['+', '*', '|']
    combinations = product(operators, repeat=operands_cnt - 1)
    return [''.join(comb) for comb in combinations]

def calculate_result(operators, operands):
    tmp = operands.copy()
    sum = int(tmp.pop(0))
    for operator in operators:
        if not operands:
            break
        match operator:
            case "+":
                sum += int(tmp.pop(0))
            case "*":
                sum *= int(tmp.pop(0))
            case "|":
                sum = int(str(sum)+tmp.pop(0))
            case _:
                raise ValueError(f"Operator is different? o,O -- {operator}")
    return sum

def find_right_operator(eqs):
    sum = 0
    for eq in eqs:
        result = eq[0]
        operands = eq[1]
        operator_possibilities = create_operator_combinations(len(operands))
        for operators in operator_possibilities:
            potential_result = calculate_result(operators, operands)
            if potential_result == int(result):
                sum += potential_result
                break
            
    return sum

if __name__ == "__main__":
    with open("day7_input.txt", 'r') as f:
        input = f.read().split('\n')
        equations = [(eq.split(':')[0].strip(), eq.split(':')[1].strip().split(" ")) for eq in input]

        sum = find_right_operator(equations)
        print(sum)