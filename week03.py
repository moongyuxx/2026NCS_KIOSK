import numpy as np

data1 = np.array([40, 30., 20, 10])
print(data1)

data2 = np.array([[1,2], [3,4]])
print(data2)

data3 = np.zeros((3, 4, 2))
print(data3)

data4 = np.ones((2,3))
print(data4)

data5 = np.array(["1", "40", "응"])
print(data5)

data6 = np.array(['300', '3333'], dtype=object)

print(data1.dtype, data2.dtype, data3.dtype, data4.dtype, data5.dtype, data6.dtype)