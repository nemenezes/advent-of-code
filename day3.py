"""Day 3"""

import numpy as np


def get_raw_data():
    with open("data/input_day3.txt", "r") as f:
        input_list = f.readlines()
        f.close()
    return input_list


def get_data_as_integers(input_list):
    output = []
    for string in input_list:
        string = string.strip()
        output.append(list(map(int, list(string))))
    return output


def get_input_data_as_array():
    input_list = get_raw_data()
    input_as_ints = get_data_as_integers(input_list)
    matrix = np.array(input_as_ints)
    return matrix










if __name__ == "__main__":
    print(get_input_data_as_array())