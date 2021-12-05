"""Day 3: Binary Diagnostic"""

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


def calculate_epsilon_gamma(matrix):
    # Return epsilon and gamma as strings
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    epsilon = []
    gamma = []

    for i in range(0, num_cols):
        col_total = sum(matrix[:,i])
        if col_total >= (num_rows/2):
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    epsilon = "".join(epsilon)
    gamma = "".join(gamma)
    return epsilon, gamma


def calculate_power_output(epsilon_str, gamma_str):
    epsilon_decimal = int(epsilon_str, 2)
    gamma_decimal = int(gamma_str, 2)
    power = epsilon_decimal * gamma_decimal
    return power
    

def calculate_o2_co2_ratings(matrix, o2_generator=True):
    # Returns string of binary representation
    num_cols = len(matrix[0])
    current_matrix = matrix
    output = []
    for i in range(0, num_cols):
        column_total = sum(current_matrix[:,i])
        num_rows = len(current_matrix)
        print(column_total)
        if o2_generator:
            chosen_val = int((column_total >= (num_rows/2)))
        else:
            chosen_val = int((column_total <= (num_rows/2)))
        print(chosen_val)
        output.append(chosen_val)
        mask = (current_matrix[:, i] == chosen_val)
        current_matrix = current_matrix[mask, :]
    output = [str(x) for x in output]
    rating = "".join(output)
    return rating


def calculate_life_support_rating(o2_generator, co2_scrubber):
    life_support = int(o2_generator, 2) * int(co2_scrubber, 2)
    return life_support

if __name__ == "__main__":
    print("Part 1")
    matrix = get_input_data_as_array()
    epsilon, gamma = calculate_epsilon_gamma(matrix)
    print(f"epsilon: {epsilon}")
    print(f"gamma: {gamma}")
    power_output = calculate_power_output(epsilon, gamma)
    print(f"power output: {power_output}")
    print("-----")
    print("Part 2")
    o2_rating = calculate_o2_co2_ratings(matrix, True)
    co2_rating = calculate_o2_co2_ratings(matrix, False)
    life_support_rating = calculate_life_support_rating(o2_rating, co2_rating)
    print(f"oxygen generator rating: {o2_rating}")
    print(f"CO2 scrubber rating: {co2_rating}")
    print(f"life support rating: {life_support_rating}")