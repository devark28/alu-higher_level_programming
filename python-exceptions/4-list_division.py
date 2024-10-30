#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    for i in range(list_length):
        try:
            result = []
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
        except TypeError:
            result.append(0)
            print("wrong type")
        # except Exception as e:
        #     result.append(0)
        #     print(e.args)
        finally:
            return result

print(list_division([10, 0, 4], [2, 4, 0], 3)) # [5.0]