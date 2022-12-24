from typing import Optional
import numpy as np

def xy_array_as_string(array,
                       mapping: dict[int, str],
                       hspace: Optional[bool]=False) -> str:
    string_array = np.empty_like(array, dtype=str)
    for i, row in enumerate(array):
        for j, n in enumerate(row):
            string_array[i, j] = mapping.get(n)
    hjoin = ' ' if hspace else ''
    return '\n'.join([hjoin.join(row) for row in string_array.T])