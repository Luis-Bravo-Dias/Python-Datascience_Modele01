import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided
    start and end arguments."""

    if not isinstance(family, list):
        print("Error: Invalid value type, use lists")
        return

    if len(family) == 0:
        print("Error: The list shouldn't be empty")
        return

    for row in family:
        if not isinstance(row, list):
            print("Error: It should be a list of lists")
            return

    first_len = len(family[0])

    for row in family:
        if len(row) != first_len:
            print("Error: Lists are not the same size")
            return

    fam = np.array(family)
    rows_1, cols_1 = fam.shape
    print(f"My shape is : ({rows_1}, {cols_1})")

    slicer = family[start:end]

    s = np.array(slicer)
    rows_2, cols_2 = s.shape
    print(f"My new shape is : ({rows_2}, {cols_2})")

    return slicer
