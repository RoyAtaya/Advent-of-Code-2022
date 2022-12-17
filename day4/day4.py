def parse_data(data):
    items = []
    for line in data:
        section_assignment_1, section_assignment_2 = line.split(',')
        low_1, high_1 = section_assignment_1.split('-')
        low_2, high_2 = section_assignment_2.split('-')
        items.append((int(low_1), int(high_1), int(low_2), int(high_2)))
    data.seek(0)
    return items

def task_1(data):
    number_of_overlap_assignment_pairs = 0
    for low_1, high_1, low_2, high_2 in data:
        if (low_1 <= low_2 and high_2 <= high_1) or (low_2 <= low_1 and high_1 <= high_2):
            number_of_overlap_assignment_pairs += 1
    return number_of_overlap_assignment_pairs

def task_2(data):
    number_of_overlap_assignment_pairs = 0
    for low_1, high_1, low_2, high_2 in data:
        if (low_1 <= low_2 and low_2 <= high_1) or (low_2 <= low_1 and low_1 <= high_2):
            number_of_overlap_assignment_pairs += 1
    return number_of_overlap_assignment_pairs

if __name__ == "__main__":
    data = open("input.txt", "r")
    data = parse_data(data)
    number_of_overlap_assignment_pairs_for_task_1 = task_1(data)
    print("Task 1:\n  The number of assignment pairs where one range fully contain the other is:", number_of_overlap_assignment_pairs_for_task_1)
    number_of_overlap_assignment_pairs_for_task_2 = task_2(data)
    print("Task 2:\n  The number of assignment pairs where there is any overlap:", number_of_overlap_assignment_pairs_for_task_2)