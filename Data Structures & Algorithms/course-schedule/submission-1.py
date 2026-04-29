class GraphNode:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph_hash = {}

        # create graph
        for p in prerequisites:
            print("CREATE GRAPH")
            print(p)
            course, preq = p
            course_node, preq_node = None, None

            if(preq not in graph_hash):
                preq_node = GraphNode(preq, [])
                graph_hash[preq] = preq_node

            if(course not in graph_hash):
                course_node = GraphNode(course, [])
                graph_hash[course] = course_node

            preq_node = graph_hash[preq]
            course_node = graph_hash[course]
            preq_node.neighbors.append(course_node)

        # detect loop using DFS from root and its neighbor
        def dfs(node, is_visited):
            print("START")
            print(node.val)
            print(node.neighbors)
            print(is_visited)
            if(len(node.neighbors) == 0):
                print("EDGE GRAPH")
                return True
            if(node.val in is_visited):
                print("LOOP")
                return False
            for neighbor in node.neighbors:
                print("NEIGHBOR")
                print(neighbor.val)
                is_visited.add(node.val)
                if not dfs(neighbor, is_visited):
                    return False
                is_visited.remove(node.val)
            return True
        
        # go through all roots
        for key, val in graph_hash.items():
            if not dfs(val, set()):
                return False
        return True