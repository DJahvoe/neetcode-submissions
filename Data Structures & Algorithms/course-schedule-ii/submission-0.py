class GraphNode:
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph_hash = {}
        res = []

        # create graph: course -> preq
        for p in prerequisites:
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
            course_node.neighbors.append(preq_node)
            print(preq_node.val)
            print(preq_node.neighbors)
            print(course_node.val)
            print(course_node.neighbors)

        print("RES INIT")
        print(res)

        # detect loop using DFS from root and its neighbor
        def dfs(node, is_visited):
            nonlocal res
            print(node.val, is_visited)
            # if course already taken, skip
            if(node.val in res):
                print("VISITED")
                return True
            # if course is in a loop, return
            if(node.val in is_visited):
                print("LOOP")
                return False
            # if course with no preq, add to result
            if(len(node.neighbors) == 0):
                print("NO PREQ")
                res.append(node.val)
                return True
                
            for neighbor in node.neighbors:
                is_visited.add(node.val)
                if not dfs(neighbor, is_visited):
                    return False
                is_visited.remove(node.val)
            res.append(node.val)
            return True

        # initially add remaining courses to res (it has no preq)
        for i in range(numCourses):
            # if course is isolated (no preq, no course that preq this course), add to the result
            if i not in graph_hash:
                res.append(i)
            else:
                # go through all preq
                if not dfs(graph_hash[i], set()):
                    return []
            print(res)
        print(res)
        return res