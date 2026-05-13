def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Takes 2 lists of integers or floats in input and returns a list
    of BMI values."""

    if not isinstance(height, list) or not isinstance(weight, list):
        print("Error: Height and weight must be lists")
        return

    if len(height) != len(weight):
        print("Error: Lists must have the same size")
        return

    bmi = []

    for h, w in zip(height, weight):

        if not isinstance(h, (int, float)) \
           or not isinstance(w, (int, float)):
            print("Error: Invalid value type, use int or float")
            return

        if h <= 0 or w <= 0:
            print("Error: Height and Weight cannot be zero or negative")
            return

        bmi.append(w / (h * h))

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Accepts a list of integers or floats and an integer representing
    a limit as parameters.
    It returns a list of booleans (True if above the limit)."""

    if not isinstance(bmi, list):
        print("Error: BMI must be a list")
        return

    if not isinstance(limit, int):
        print("Error: Invalid value type, use int for the limit")
        return

    result = []

    for value in bmi:

        if not isinstance(value, (int, float)):
            print("Error: Invalid value type, use int or float")
            return

        if value > limit:
            result.append(True)
        else:
            result.append(False)

    return result
   
