#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    result = 0
    for x in range(0, list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            result = 0
            print("Wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result  = 0
            print("out of range")
        finally:
            pass
        new.append(result)
    return new
