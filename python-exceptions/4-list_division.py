#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        try:
            result = []
            result.append(my_list_1[i] / my_list_2[i])
        except Exception as e:
            result.append(0)
            print(e.args[0])
            if e.args[0] == 'list index out of range':
                print("out of range")
            elif e.args[0] == 'division by zero':
                print("division by 0")
            else:
                # print("wrong type")
        finally:
            return result
    print()
