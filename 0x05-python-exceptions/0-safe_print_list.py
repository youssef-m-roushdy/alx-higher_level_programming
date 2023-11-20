def safe_print_list(my_list=None, x=0):
    try:
        if my_list is None:
            my_list = []  # Create an empty list if my_list is not provided
        count = 0
        while count < x:
            print("{}".format(my_list[count]), end="")
            count += 1
        print("")
        return count
    except IndexError:
        print("")
        return count
