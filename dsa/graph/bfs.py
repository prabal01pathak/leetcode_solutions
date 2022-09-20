from typing import List
from collections import deque


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def bfs(graph: List[str], first: str) -> List[str]:
    queue = deque([ first ])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for i in graph[node]:
            queue.append(i)
    return result



def test_bfs() -> None:
    """ test dfs function """
    result = bfs(graph, "a")
    print("iterative: ", result)
    assert result == ["a", "b", "c", "d", "e", "f"]

if __name__ == "__main__":
    test_bfs()
    print(10*"=", " Passed tests ", 10*"=")
