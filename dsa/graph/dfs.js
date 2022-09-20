const assert = require("assert")

const dfs = (graph, first) => {
    const stack = [ first ]
    const result = []
    while (stack.length > 0) {
        node = stack.pop()
        for (let i of graph[node]){
            stack.push(i)
        }
        result.push(node)
    }
    return result
}


const dfsRecursive = (graph, first) => {
    const recursive = (value) => {
        result.push(value)
        for (let v of graph[value]) {
            recursive(v)
        }
    }
    result = []
    recursive("a")
    return result
} 


test_dfs = () => {
    const graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": []
    }
    let data = dfsRecursive(graph, "a")
    let dataIterative = dfs(graph, "a")
    const output = ["a", "b", "d", "f", "c", "e"]
    const outputIterative = [ 'a', 'c', 'e', 'b', 'd', 'f' ]
    assert(JSON.stringify(data) == JSON.stringify(output))
    assert(JSON.stringify(dataIterative) == JSON.stringify(outputIterative))
}


test_dfs()
console.log("Test passert ==>")
