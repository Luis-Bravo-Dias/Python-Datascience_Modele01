import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
 
 fam = np.array(family)
 rows_1, cols_1 = fam.shape
 print(f"My shape is : ({rows_1}, {cols_1})")
 slicer = family[start:end]
 s = np.array(slicer)
 rows_2, cols_2 = s.shape
 print(f"My new shape is : ({rows_2}, {cols_2})")
 return slicer