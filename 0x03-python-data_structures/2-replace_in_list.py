#!/usr/bin/python3
if __name__ == "__main__":
    def replace_in_list(my_list, idx, element):
        if idx < 0 or idx > len(my_list):
            return my_list
        mylist[idx] = element
        return my_list
