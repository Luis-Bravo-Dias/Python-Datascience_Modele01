def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
 """Takes 2 lists of integers or floats in input and returns a list
of BMI values."""
 if len(height) != len(weight):
    raise ValueError("Lists must have the same size")
 bmi = []
 for h, w in zip(height, weight):
   if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
     raise TypeError("Invalid value type, use int or float")
   if h <= 0 or w <= 0:
    raise ValueError("Height and Weight cannot be zero or negative")
   bmi.append(w / (h * h))
 return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
 if not isinstance(limit, int):
  """Accepts a list of integers or floats and an integer representing
a limit as parameters.
It returns a list of booleans (True if above the limit)."""
  raise TypeError("Invalid value type, use int for the limit")
 result = []
 for i in range(len(bmi)):
   if not isinstance(bmi[i], (int, float)):
     raise TypeError("Invalid value type, use int or float for the list items")
   else:
    if bmi[i] > limit:
     result.append(True)
    else:
     result.append(False)
 return result
   
