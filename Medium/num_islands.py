'''
200. Number of Islands
Rating: Medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Notes:
DFS, time and space are both O(M x N) i.e. O(rows x cols)
'''



class Solution:
    def dfs(self, grid, row, col):
        num_rows = len(grid)
        num_cols = len(grid[0])

        # If we go out of bounds or we hit a 0, we can stop and trigger a new search
        if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
            return
        if grid[row][col] == '0':
            return

        # Otherwise, mark the current location as searched, then keep searching
        grid[row][col] = '0'
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)

    def numIslands(self, grid):
        if grid == None or len(grid) == 0:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands


arr = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
s = Solution()
print(s.numIslands(arr))