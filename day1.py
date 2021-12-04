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


def add_differences(df):
    df["depth_diff"] = df["depth"].diff(periods=1)
    df["depth_rolling_sum"] = df["depth"].rolling(3).sum()
    df["rolling_sum_diff"] = df["depth_rolling_sum"].diff(periods=1)
    df["type_of_change_prev_day"] = df["depth_diff"].apply(type_of_change)
    df["type_of_change_rolling_sum"] = df["rolling_sum_diff"].apply(type_of_change)
    return df


def print_changes(df):
    df = get_raw_data()
    df = add_differences(df)
    print("Change since previous measurement:")  # noqa
    print(df["type_of_change_prev_day"].value_counts())  # noqa
    print("Change in rolling sum:")  # noqa
    print(df["type_of_change_rolling_sum"].value_counts())  # noqa


if __name__ == "__main__":
    df = get_raw_data()
    print_changes(df)
