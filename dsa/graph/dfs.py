from typing import List

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


def dfs(graph: dict) -> List[str]:
    """ traverse the graph in dfs order """
    keys = graph.keys()
    iterator = iter(keys)
    result = []
    stack = [ next(iterator) ]
    while stack:
        node = stack.pop()
        result.append(node)
        for i in graph[node]:
            stack.append(i)
    return result


def dfs_recursive(graph: dict) -> List[str]:
    """ traverse the graph in dfs order recursiverly """
    def recursive(value: str) -> List[str]:
        result.append(value)
        for i in graph[value]:
            recursive(i)

    keys = graph.keys()
    iterator = iter(keys)
    result = []
    recursive(next(iterator))
    return result


def test_dfs() -> None:
    """ test dfs function """
    result = dfs_recursive(graph)
    result2 = dfs(graph)
    print("recursive: ", result)
    print("iterative: ", result)
    assert (
        (result == ["a", "c", "e", "b", "d", "f"]
        or result == ["a", "b", "d", "f", "c", "e"])
        and
        (result2 == ["a", "c", "e", "b", "d", "f"]
        or result2 == ["a", "b", "d", "f", "c", "e"])
    )

if __name__ == "__main__":
    test_dfs()
    print(10*"=", " Passed tests ", 10*"=")
