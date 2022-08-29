class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        rows, cols = len(board), len(board[0])
        path = set()
        res = set()
        
        def dfs(r, c , node, word):
            if (
                (r< 0 or c < 0) or
                (r >= rows or c >= cols) or
                ((r,c ) in path) or
                (board[r][c] not in node.children)
            ):
                return False
            path.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            path.remove((r,c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root, "")
        return  res
# time complexity: O(n*m*4^n)