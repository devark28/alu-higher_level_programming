#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        try:
            result = []
            result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            result.append(0)
            print("out of range")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        finally:
            return result
