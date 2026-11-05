class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.seen = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in self.seen:
                    count += 1
                    self.dfs((i,j),grid)
        return count
    def dfs(self,node,grid):
        if node[0]>=len(grid) or node[0] < 0:
            return
        if node[1]>=len(grid[0]) or node[1] < 0:
            return
        if grid[node[0]][node[1]] == '0':
            return
        if node in self.seen:
            return
        self.seen.add(node)
        i,j = node[0],node[1]
        check = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        for n in check:
            self.dfs(n,grid)

