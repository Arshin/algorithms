class Solution:
    def func(self, bombs, row, col):
        field = [[0 for i in range(col)] for j in range(row)]

        for bomb in bombs:
            bomb_col = bomb[0]
            bomb_row = bomb[1]
            field[bomb_col][bomb_row] = -1

            for i in range(bomb_col-1, bomb_col+2):
                for j in range(bomb_row-1, bomb_col+2):
                    print(i,j)
                    if (0 <= i < col) and (0 <= j < row) and (field[i][j] != -1):
                        field[i][j] += 1

        return field

tmp = Solution()
print(tmp.func([[0,0], [1,2]], 3, 4))
