import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
 
 if not isinstance(family, list):
  raise TypeError("Invalid value type, use lists")
 if len(family) == 0:
  raise TypeError("The list shouldn't be empty")
 for row in family:
    if not isinstance(row, list):
        raise TypeError("It should be a list of lists")
 first_len = len(family[0])
 for row in family:
  if len(row) != first_len:
   raise TypeError("Invalid value type, use int or float")
 fam = np.array(family)
 rows_1, cols_1 = fam.shape
 print(f"My shape is : ({rows_1}, {cols_1})")
 slicer = family[start:end]
 s = np.array(slicer)
 rows_2, cols_2 = s.shape
 print(f"My new shape is : ({rows_2}, {cols_2})")
 return slicer