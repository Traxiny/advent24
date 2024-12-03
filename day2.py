import csv 


def check_monotonicity(a, b):
    # The levels are either all increasing or all decreasing.
    # 99 98 96 94 88 91 85
    if a > b:
        return True
    
    return False

def in_acceptable_range(a, b):
    # Any two adjacent levels differ by at least one and at most three.
    return 1 <= abs(a - b) <= 3 

def is_report_safe(report: list):
    max_i = len(row)
    last_monotonicity = None
    for i in range(1, max_i):
        current_monotonicity = check_monotonicity(int(report[i-1]), int(report[i]))
        if last_monotonicity is None:
            last_monotonicity = current_monotonicity
        if not in_acceptable_range(int(report[i-1]), int(report[i])) or current_monotonicity != last_monotonicity:
            return False
    
    return True


if __name__ == "__main__":
    safe_reports = 0
    with open("day2_input.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            safe_reports += is_report_safe(row)
    print(safe_reports)