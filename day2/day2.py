def switch(item):
    if "A" in item or "X" in item:
        return "R"
    elif "B" in item or "Y" in item:
        return "P"
    elif "C" in item or "Z" in item:
        return "S"

def convert_player_choice_to_points(player_choice):
    if player_choice == "R":
        return 1
    elif player_choice == "P":
        return 2
    elif player_choice == "S":
        return 3
        
def get_points(player_choice, elf_choice, task):    
    # outcomes are ordered as such : (player_choice, elf_choice)
    possible_outcomes_for_draw = [("R", "R"), ("P", "P"), ("S", "S")]
    possible_outcomes_for_player_win = [("R", "S"), ("P", "R"), ("S", "P")]
    possible_outcomes_for_elf_win = [("S", "R"), ("R", "P"), ("P", "S")]
    
    if task == "TASK1":
        player_points = convert_player_choice_to_points(player_choice)
        if (player_choice, elf_choice) in possible_outcomes_for_draw:
            return player_points + 3
        elif (player_choice, elf_choice) in possible_outcomes_for_player_win:
            return player_points + 6
        elif (player_choice, elf_choice) in possible_outcomes_for_elf_win:
            return player_points
    else:
        if player_choice == "X":
            # player needs to lose
            for outcome in possible_outcomes_for_elf_win:
                if elf_choice == outcome[1]:
                    return convert_player_choice_to_points(outcome[0])
        elif player_choice == "Y":
            # player needs to draw
            for outcome in possible_outcomes_for_draw:
                if elf_choice == outcome[1]:
                    return convert_player_choice_to_points(outcome[0]) + 3
        elif player_choice == "Z":
            # player needs to draw
            for outcome in possible_outcomes_for_player_win:
                if elf_choice == outcome[1]:
                    return convert_player_choice_to_points(outcome[0]) + 6

if __name__ == "__main__":
    data = open("input.txt","r")
    elf_moves = []
    player_moves = []
    total_points_part_1 = 0
    total_points_part_2 = 0
    for line in data:
        elf_moves.append(switch(line[:1]))
        player_moves.append((line[2:3], switch(line[2:])))
    
    for idx in range(len(elf_moves)):
        total_points_part_1 += get_points(player_moves[idx][1], elf_moves[idx], "TASK1")
        total_points_part_2 += get_points(player_moves[idx][0], elf_moves[idx], "TASK2")
        
    print('Part 1: Total points =', total_points_part_1)
    print('Part 2: Total points =', total_points_part_2)
    data.close()