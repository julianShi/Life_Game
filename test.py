from Life import Life

life=Life()

# For test
M = [[1, 0, 1, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 0, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 1, 0, 0]]

X=life.one_step(M) # next step
life.show_matrix(X)
