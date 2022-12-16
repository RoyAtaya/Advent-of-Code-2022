def parse_data(data, task):
    items = []
    if task == 1:
        for line in data:
            if "\n" in line:
                items.append((line[:(len(line)-1)//2] , line[(len(line)-1)//2:len(line)-1]))
            else:
                items.append((line[:(len(line))//2] , line[(len(line))//2:len(line)]))
    else:
        idx = 0
        temp_arr = []
        for line in data:
            temp_arr.append(line[:len(line)-1])
            idx += 1
            if idx == 3:
                items.append(temp_arr)
                temp_arr = []
                idx = 0
    data.seek(0)
    return items

def task1(data):
    items = parse_data(data, 1)
    extra_letters = []
    
    for elem1, elem2 in items:
        for idx in range(len(elem1)):
            if elem1[idx] in elem2:
                extra_letters.append(elem1[idx])
                break
            
    return extra_letters

def three_elem_min(a, b, c):
    if (a <= b) and (a <= c):
        return (a, "elem1") 
    elif (b <= a) and (b <= c):
        return (b, "elem2") 
    else:
        return (c, "elem3") 

def find_extra_letters_task2(min_length, elem_to_search, elem_to_be_searched_1, elem_to_be_searched_2):
    for idx in range(min_length):
        if elem_to_search[idx] in elem_to_be_searched_1 and elem_to_search[idx] in elem_to_be_searched_2:
            return elem_to_search[idx]

def task2(data):
    items = parse_data(data, 2)
    extra_letters = []
    
    for elem1, elem2, elem3 in items:
        min_length, min_elem = three_elem_min(len(elem1), len(elem2), len(elem3))
        if min_elem == "elem1":
            extra_letters.append(find_extra_letters_task2(min_length, elem1, elem2, elem3))
        elif min_elem == "elem2":
            extra_letters.append(find_extra_letters_task2(min_length, elem2, elem1, elem3))
        else:
            extra_letters.append(find_extra_letters_task2(min_length, elem3, elem1, elem2))
            
    return extra_letters

def get_total_sum(priorities, task_array):
    total_task_sum = 0
    
    for letter in task_array:
        total_task_sum += priorities[letter]
        
    return total_task_sum

if __name__ == "__main__":
    data = open("day3.txt", "r")
    priorities = {}
    task_1_total_sum = 0
    task_2_total_sum = 0
    
    for i in range(1, 27):
        priorities[chr(122 - 26 + i)] = i # assign each lower case letter to 1 - 26
        priorities[chr(90 - 26 + i)] = 26 + i # assign each upper case letter to 27 - 52

    task_1_array = task1(data)
    task_2_array = task2(data)
    
    task_1_total_sum = get_total_sum(priorities, task_1_array)
    task_2_total_sum = get_total_sum(priorities, task_2_array)
    
    print("task 1: ", task_1_total_sum)
    print("task 2: ", task_2_total_sum)
    
    data.close()