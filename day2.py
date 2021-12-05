"""
Day 2: Dive!
"""
INITIAL_POSITION = (0, 0)
FORWARD = "forward"
DOWN = "down"
UP = "up"


def get_raw_data():
    with open("data/input_day2.txt", "r") as f:
        input_list = f.readlines()
        f.close()
    return input_list
        

def calc_new_position(starting_position, direction, units_to_move):
    horizontal_pos = starting_position[0]
    vertical_pos = starting_position[1]
    if direction == UP:
        vertical_pos = vertical_pos - units_to_move
    elif direction == DOWN:
        vertical_pos = vertical_pos + units_to_move
    elif direction == FORWARD:
        horizontal_pos = horizontal_pos + units_to_move
    new_position = (horizontal_pos, vertical_pos)
    return new_position


def get_final_pos(start_position, input_commands):
    position = start_position
    for command in input_commands:
        command = command.split()
        direction = command[0]
        units = int(command[1])
        position = calc_new_position(position, direction, units_to_move=units)
    return position


if __name__ == "__main__":
    input_commands = get_raw_data()
    final_pos = get_final_pos(INITIAL_POSITION, input_commands)
    print("Final position:")
    print(final_pos)
    print("Multiply:")
    print(final_pos[0]*final_pos[1])