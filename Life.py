import numpy as np
import matplotlib.pyplot as plt


def life():
    # print('Enter seeds location:')
    # M = eval(input())

    # For test
    M = [[1, 0, 1, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 1, 0, 0]]
    M = np.pad(M, ((1, 1), (1, 1)), 'constant')
    M = np.array(M)
    L, W = np.shape(M)
    X = np.zeros((L, W))
    for i in range(1, L - 1):
        for j in range(1, W - 1):
            sub_matrix = M[i - 1:i + 2, j - 1:j + 2]
            # Any live cell with fewer than two live neighbors dies, as if by underpopulation
            if M[i, j] == 1 and np.count_nonzero(sub_matrix == 1) < 2:
                X[i, j] = 0
            # Any live cell with two or three live neighbors lives on to the next generation
            if M[i, j] == 1 and np.count_nonzero(sub_matrix == 1) in (2, 3):
                X[i, j] = M[i, j]
            # Any live cell with more than three live neighbors dies, as if by overpopulation
            if M[i, j] == 1 and np.count_nonzero(sub_matrix == 1) > 3:
                X[i, j] = 0
            # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
            if M[i, j] == 0 and np.count_nonzero(sub_matrix == 1) == 3:
                X[i, j] = 1
    X = X[1:L - 1, 1:W - 1]
    print("here is the next patten")
    print(X)
    img = plt.imshow(X)
    img.set_cmap('winter')
    plt.show()
    return X


# Run file
life()
