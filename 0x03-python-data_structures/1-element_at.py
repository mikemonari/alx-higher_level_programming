#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        else:
            print("Element at index {} is {}".format(idx, my_list[idx]))