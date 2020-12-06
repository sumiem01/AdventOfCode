"""Useful functions for general purposes of Advent of Code"""


def get_data(path: str) -> list:
    with open(path, "r") as f:
        return f.readlines()
