import random
import itertools
from collections import Counter

def flush(suit_list):
    suit_set = itertools.combinations(suit_list,5)

    for fi_list in suit_set:
        for fi in range(5):
            if fi_list[fi] != fi_list[fi+1]:
                break
            if fi == 4:
                return True
    return False

def straight(point_list):
    point_set = itertools.combinations(point_list,5)
    final_list = []

    for si_list in point_set:
        for si in range(0,5):
            if si_list[si+1] != si_list[si]:
                break
            if si == 4:
                final_list = si_list

    return final_list

def create_pair_dir(point_list):
    pair_dir = {}

    for pi in range(0, 5):
        if point_list[pi] in pair_dir:
            pair_dir[point_list[pi]] += 1
        else:
            pair_dir[point_list[pi]] = 1

    return pair_dir

def one_pair(point_list):
    pair_dir = create_pair_dir(point_list)

    for pi in pair_dir:
        if pair_dir[pi] == 2:
            return True
        else:
            return False


def two_pair(point_list):
    pair_dir = create_pair_dir(point_list)
    pair_set = set(pair_dir.values())

    if 2 in pair_dir.values() and len(pair_set) - len(pair_dir) == -2:
        return True
    else:
        return False


def three_of_a_kind(point_list):
    pair_dir = create_pair_dir(point_list)

    for ti in pair_dir:
        if pair_dir[ti] == 3:
            return True
        else:
            return False


def four_of_a_kind(point_list):
    pair_dir = create_pair_dir(point_list)

    if 4 in pair_dir.values():
        return True
    else:
        return False

def full_house(point_list):
    pair_dir = create_pair_dir(point_list)

    if 2 in pair_dir.values() and 3 in pair_dir.values():
        return True
    else:
        return False
def high_card(point_list):
    return max(point_list)

def straight_flush(point_list,suit_list):
    if flush(suit_list):
        if straight(point_list):
            return straight(point_list)
