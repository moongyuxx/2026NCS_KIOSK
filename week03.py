import numpy as np
import pandas as pd

#      a   b    c
# 1  100  95   70
# 2   80  75  100
# 3   90  85   99

# items = {"a":[100,80,90],
#          "b":[95,75,85],
#          "c":[70,100,99]}

items = [
    [100,80,90],
    [95,75,85],
    [70,100,99]
]

df_items = pd.DataFrame(items, index=[1,2,3], columns=["a","b","c"])
print(df_items)