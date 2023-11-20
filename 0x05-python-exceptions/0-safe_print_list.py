
def safe_print_list(my_list=[], x=0):
    try:
        if x > len(my_list):
            x = len(my_list)
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
        print("")
        return x
    except IndexError:
        print("Index out of range")
        return 0
