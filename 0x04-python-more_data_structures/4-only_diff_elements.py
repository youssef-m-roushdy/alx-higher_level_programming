#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_diff_list = list(set_1.difference(set_2)) + list(set_2.difference(set_1))
    return only_diff_list
