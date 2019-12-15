import numpy as np
import matplotlib.pyplot as plt

#лямбда
y = 0.005
#мю
u = 0.001
#время
t = 1000
#шаг времени
delta = 10
#начальные условия
p0 = np.array([
    [1],
    [0],
    [0],
    [0],
    [0],
    [0]
])
#матрица интенсивностей
intensity_matrix = np.array([
    [-3*y, u,      0,      0,       0,      0],
    [3*y,  -3*y-u, u,      0,       0,      0],
    [0,    3*y,    -3*y-u, u,       0,      0],
    [0,    0,      3*y,    -3*y-u,  u,      0],
    [0,    0,      0,      3*y,     -2*y-u, u],
    [0,    0,      0,      0,       2*y,    -u]
])

########################################################
# y = 0.005
# u = 0.001
# t = 5000
# delta = 10
#
# intensity_matrix = np.array([
#     [-9*y, u,      0,      0,       0,      0,      0,      0],
#     [9*y,  -9*y-u, u,      0,       0,      0,      0,      0],
#     [0,    9*y,    -9*y-u, u,       0,      0,      0,      0],
#     [0,    0,      9*y,    -9*y-u,  u,      0,      0,      0],
#     [0,    0,      0,      9*y,     -8*y-u, u,      0,      0],
#     [0,    0,      0,      0,       8*y,    -7*y-u, u,      0],
#     [0,    0,      0,      0,       0,      7*y,    -6*y-u, u],
#     [0,    0,      0,      0,       0,      0,      6*y,    -u]
# ])
# p0 = np.array([
#     [0],
#     [0],
#     [0],
#     [1],
#     [0],
#     [0],
#     [0],
#     [0]
# ])
##############################????????????

matrix_size = intensity_matrix.shape[0]
#единичная матрица
unit_matrix = np.eye(matrix_size)

#Ф(t)
f_delta = unit_matrix + \
          intensity_matrix * delta + \
          (np.linalg.matrix_power(intensity_matrix, 2) * (delta**2)) / 2 + \
          (np.linalg.matrix_power(intensity_matrix, 3) * (delta**3)) / 6

previous = p0
counter = int(t/delta)
p = np.zeros((matrix_size+1, counter+1))
p[0, 0] = 1

i = 1
while i <= counter:
    p_delta = np.matmul(f_delta, previous)

    for j in range(matrix_size):
        p[j, i] = p_delta[j]

    p[matrix_size, i] = delta * i
    previous = p_delta
    i += 1

for i in range(matrix_size):
    plt.plot(p[matrix_size], p[i], label='P(' + str(i+1) + ')')

#print(p[matrix_size])
#print(p[0])

plt.ylabel('Probability')
plt.legend()
plt.xlim(0, t)
plt.ylim(0, 1)
grid1 = plt.grid(True)
plt.show()
