class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_count += 1
                    self.dfs(grid,i,j)
                    
        return island_count
                
        
    def dfs(self,grid, i, j):
        if i < 0 or len(grid) <= i:
            return
        if j < 0 or len(grid[0]) <= j:
            return
        if grid[i][j] == "1":
            grid[i][j] = "_"
            self.dfs(grid, i+1, j)
            self.dfs(grid, i-1, j)
            self.dfs(grid, i, j+1)
            self.dfs(grid, i, j-1)

# solved this after walk through day before