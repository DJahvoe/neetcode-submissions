class Solution:
    def charDifferent(self, first, second):
        diff = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                diff += 1
        return diff

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph_hash = defaultdict(list)
        wordList.append(beginWord)
        # create graph with 1 char different
        for x in wordList:
            for y in wordList:
                if self.charDifferent(x, y) != 1:
                    continue
                graph_hash[x].append(y)
        
        q = deque([(beginWord, 1)])
        visited = set()
        res = float("inf")
        while q:
            word, step = q.popleft()
            if word == endWord:
                res = min(res, step)
            visited.add(word)
            for neighbor in graph_hash[word]:
                if neighbor in visited:
                    continue
                q.append((neighbor, step + 1))

        
        return 0 if res == float("inf") else res
        