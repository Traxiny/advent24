def parse_rules(rules: list):
    page_order = {}
    for rule in rules:
        first_num = rule.split('|')[0]
        second_num = rule.split('|')[1]
        if first_num in page_order:
            page_order[first_num].append(second_num)
        else:
            page_order[first_num] = [second_num]
    
    return page_order

def is_right_position(following_rules, previous_pages):
    for i, page in enumerate(previous_pages):
        if page in following_rules:
            return str(i)
    return None

def is_right_order(update, rules):
    for i, page in enumerate(update):
        if page not in rules:
            continue
        
        if is_right_position(rules[page], update[:i]):
            return False
    
    return True

def repair_update(following_rules, update):
    repaired_update = []
    remaining_pages = update[:]

    while remaining_pages:
        progressing = False
        print(repaired_update)
        for page in remaining_pages[:]:
            if page not in following_rules or is_right_position(following_rules[page], repaired_update) is None:
                repaired_update.append(page)
                remaining_pages.remove(page)
                progressing = True
                break
            problematic_index = int(is_right_position(following_rules[page], repaired_update))
            repaired_update.insert(problematic_index, page)
            remaining_pages.remove(page)
            progressing = True
        if not progressing:
            raise ValueError("Circular dependency")
      
    return repaired_update

def find_valid_updates(updates: list, page_positions):
    valid_updates = []
    invalid_updates = []
    for update in updates:
        update_list = update.split(',')
        if is_right_order(update_list, page_positions):
            valid_updates.append(update_list)
        else:
            invalid_updates.append(repair_update(page_positions, update_list))

    return  (valid_updates, invalid_updates)

def sum_middle_pages(updates):
    sum = 0
    for update in updates:
        middleIndex = int((len(update) - 1)/2)
        sum += int(update[middleIndex])

    return sum


if __name__ == "__main__":
    with open("day5_input.txt", 'r') as f:
        input = f.read().split('\n')
        divider_index = input.index("")
        rules = input[:divider_index]
        updates = input[divider_index+1:]
        ordered_pages = parse_rules(rules)
        valid, invalid = find_valid_updates(updates, ordered_pages)
        print(sum_middle_pages(valid))
        # part 2
        print(invalid)
        print(sum_middle_pages(invalid))