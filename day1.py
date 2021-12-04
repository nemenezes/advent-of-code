"""Day 1: Sonar Sweep"""
import pandas as pd

UNDEFINED = "undefined"
INCREASE = "increase"
DECREASE = "decrease"
NO_CHANGE = "no change"


def get_raw_data():
    df = pd.read_csv(
        "data/input_day1.txt", delimiter="\n", header=None, names=["depth"]
    )
    return df


def type_of_change(diff):
    output = UNDEFINED
    if diff > 0:
        output = INCREASE
    elif diff < 0:
        output = DECREASE
    elif diff == 0:
        output = NO_CHANGE
    return output


def add_difference(df):
    df["depth_diff"] = df["depth"].diff(periods=1)
    df["type_of_change"] = df["depth_diff"].apply(type_of_change)
    return df


def print_changes(df):
    df = get_raw_data()
    df = add_difference(df)
    print("Change since previous measurement:")  # noqa
    print(df["type_of_change"].value_counts())  # noqa


if __name__ == "__main__":
    df = get_raw_data()
    df = add_difference(df)
    print_changes(df)
