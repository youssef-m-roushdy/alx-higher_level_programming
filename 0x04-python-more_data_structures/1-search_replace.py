#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list[0:]
    my_new_list[search - 1] = replace
    return my_new_list
