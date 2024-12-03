import csv

def get_sorted_lists():
    left = []
    right = []
    with open("day1_input.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            left.append(int(row[0]))
            right.append(int(row[3]))

    left.sort() 
    right.sort()
    return (left, right)

def get_difference(sorted_l, sorted_r ):
    total_distance = 0
    for i in range(len(sorted_l)):
        total_distance += abs(sorted_l[i] - sorted_r[i])

    print(total_distance)

def get_similarity(sorted_l, sorted_r):
    seen_ids = {}
    total_similarity = 0
    for l_id in sorted_l:
        if l_id not in seen_ids.keys():
            cnt = sorted_r.count(l_id)
            seen_ids[l_id] = l_id * cnt
        
        total_similarity += seen_ids[l_id]

    print(total_similarity)

if __name__ == "__main__":
    sorted_l, sorted_r = get_sorted_lists()
    get_difference(sorted_l, sorted_r)
    get_similarity(sorted_l, sorted_r)