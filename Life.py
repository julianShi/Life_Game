import numpy as np


class Solution:
    def life(self, M):
        L = len(M)
        M = np.array(M)
        X = np.zeros((L, L))
        for i in range(1, L - 1):
            for j in range(1, L - 1):
                sub_matrix = M[i - 1:i + 2, j - 1: j + 2]
                # 当前细胞为存活状态时，当周围的存活细胞低于2个时（不包含2个）， 该细胞变成死亡状态。（模拟生命数量稀少）
                if M[i, j] == 1 and np.count_nonzero(sub_matrix == 1) < 2:
                    X[i, j] = 0
                # 当前细胞为存活状态时，当周围有2个或3个存活细胞时， 该细胞保持原样。
                if M[i, j] == 1 and np.count_nonzero(sub_matrix == 1) in (2, 3):
                    X[i, j] = M[i, j]
                # 当前细胞为存活状态时，当周围有3个以上的存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
                if M[i, j] == 1 and np.count_nonzero(sub_matrix == 1) > 3:
                    X[i, j] = 0
                # 当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。 （模拟繁殖）
                if M[i, j] == 0 and np.count_nonzero(sub_matrix == 1) == 3:
                    X[i, j] = 1
        return X


if __name__ == '__main__':
    print(Solution().life([[0, 0, 0, 0, 0, 0, 0],
                           [0, 1, 0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 1, 1, 1, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]))
