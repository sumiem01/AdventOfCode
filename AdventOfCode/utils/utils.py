"""Useful functions for general purposes of Advent of Code"""


def get_lines(path: str) -> list:
    """Extract .txt file to variable list"""
    with open(path, "r") as f:
        return f.readlines()


def get_raw_data(path: str):
    """Basically open the file and read it's content"""
    with open(path, "r") as f:
        return f.read()


def clean_input(data: list) -> list:
    """
    Remove \n characters from elements of the list
    and change numbers to integers
    """
    new_input: list = []
    for i in data:
        new_input.append(int(i.replace("\n", "")))
    return new_input


def clean_new_line_char(data: list) -> list:
    new_input: list = []
    for i in data:
        new_input.append(i.replace("\n", ""))
    return new_input
