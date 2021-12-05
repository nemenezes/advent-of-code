"""Day 2: Dive!"""

INITIAL_POSITION = (0, 0)
INITIAL_POSITION_WITH_AIM = (0, 0, 0)
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


# Uses the method set-out in part 2
def calc_new_position_with_aim(starting_position, direction, units_to_move):
    horizontal_pos = starting_position[0]
    vertical_pos = starting_position[1]
    aim = starting_position[2]
    if direction == UP:
        aim = aim - units_to_move
    elif direction == DOWN:
        aim = aim + units_to_move
    elif direction == FORWARD:
        horizontal_pos = horizontal_pos + units_to_move
        vertical_pos = vertical_pos + (aim * units_to_move)
    new_position = (horizontal_pos, vertical_pos, aim)
    return new_position


def get_final_pos(start_position, input_commands, calc_with_aim=False):
    position = start_position
    for command in input_commands:
        command = command.split()
        direction = command[0]
        units = int(command[1])
        if calc_with_aim:
            position = calc_new_position_with_aim(
                position, direction, units_to_move=units
            )
        else:
            position = calc_new_position(position, direction, units_to_move=units)
    return position


if __name__ == "__main__":
    input_commands = get_raw_data()
    print("Part 1")
    final_pos = get_final_pos(INITIAL_POSITION, input_commands)
    print("Final position:")
    print(final_pos)
    print("Multiply:")
    print(final_pos[0] * final_pos[1])
    print("----")
    print("Part 2")
    final_pos = get_final_pos(
        INITIAL_POSITION_WITH_AIM, input_commands, calc_with_aim=True
    )
    print("Final position:")
    print(final_pos)
    print("Multiply:")
    print(final_pos[0] * final_pos[1])
