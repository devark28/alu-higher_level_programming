#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
# print(best_score({'John': 100, 'Bob': 300, 'Mike': 200, 'Sarah': 500}))
