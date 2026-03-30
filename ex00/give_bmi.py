def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:

 if len(height) != len(weight):
    raise ValueError("Lists must have the same size")
 bmi = []
 for h, w in zip(height, weight):
   if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
     raise TypeError("Invalid value type")
   if h <= 0 or w <= 0:
    raise ValueError("Height and Weight cannot be zero or negative")
   bmi.append(w / (h * h))
 return bmi

#def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here

