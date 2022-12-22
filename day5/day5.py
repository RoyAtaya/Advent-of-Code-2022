from collections import deque
from math import ceil
from copy import deepcopy
from itertools import islice

def get_and_parse_data(filename):
    """get and parse data from input file

    Args:
        filename (_type_): name of input file

    Returns:
        moves: list of moves as a tuple
        starting positions: list of starting positions
    """
    starting_positions = []
    moves = []
    with open(filename) as f:
        idx = 0
        for line in f:
            if line.startswith("move"):
                moves.append(line.rstrip())
            elif len(line) > 0 and '1' not in line:
                m = ceil((len(line) - 1)/ 4)
                i = 1
                k = 0
                if idx == 0:
                    for j in range(m):
                        starting_positions.append(deque())
                    idx = 1
                
                while i < len(line):
                    if line[i] != ' ':
                        starting_positions[k].appendleft(line[i])
                    i = i + 4
                    k = k + 1
    return moves, starting_positions

def move_crates(moves, crates):
    crates = deepcopy(crates)
    for curr_move in moves:
        _, amount, _, start_pile, _, end_pile = curr_move.split(' ')
        amount, start_pile, end_pile = int(amount), int(start_pile) - 1, int(end_pile) - 1 # subtract 1 to make the start_pile and end_pile be zero indexed 
        for amt in range(amount):
            for pile_idx in range(len(crates)):
                if pile_idx == start_pile:
                    crates[end_pile].append(crates[start_pile][-1])
                    crates[start_pile].pop()
    return crates
                        
def get_top_crates_from_each_pile(crates):
    top_crates = []
    for idx in range(len(crates)):
        top_crates.append(crates[idx][-1])
    return ''.join(top_crates)
        
def move_crates_task2(moves, crates):
    crates = deepcopy(crates)
    for curr_move in moves:
        _, amount, _, start_pile, _, end_pile = curr_move.split(' ')
        amount, start_pile, end_pile = int(amount), int(start_pile) - 1, int(end_pile) - 1 # subtract 1 to make the start_pile and end_pile be zero indexed 
        for pile_idx in range(len(crates)):
            if pile_idx == start_pile:
                crates[end_pile].extend(list(islice(crates[start_pile], len(crates[start_pile]) - amount, len(crates[start_pile]))))
                for i in range(amount):
                    crates[start_pile].pop()
    return crates

if __name__ == "__main__":
        moves, starting_positions = get_and_parse_data("input.txt")
        crates = move_crates(moves, starting_positions)
        top_crates = get_top_crates_from_each_pile(crates)
        crates2 = move_crates_task2(moves, starting_positions)
        top_crates2 = get_top_crates_from_each_pile(crates2)
        print('---------------Task 1----------------')
        print("Top crates for task 1: ", top_crates)
        print('---------------Task 2----------------')
        print("Top crates for task 2: ", top_crates2)