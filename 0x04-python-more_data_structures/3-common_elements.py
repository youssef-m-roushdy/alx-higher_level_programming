#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []
    for word1 in set_1:
        for word2 in set_2:
            if word1 == word2:
                common_list.append(word1)
    return common_list
