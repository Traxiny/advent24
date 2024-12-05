import csv 

def problem_damper(report: list):
    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if is_report_safe(temp_report):
            return True
    return False

def check_monotonicity(a, b):
    # The levels are either all increasing or all decreasing.
    # 99 98 96 94 88 91 85
    return a > b

def in_acceptable_range(a, b):
    # Any two adjacent levels differ by at least one and at most three.
    return 1 <= abs(a - b) <= 3 

def is_report_safe(report: list):
    max_i = len(report)
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
            cur_report = is_report_safe(row)
            if not cur_report:
                cur_report = problem_damper(row)
            safe_reports += cur_report
    print(safe_reports)