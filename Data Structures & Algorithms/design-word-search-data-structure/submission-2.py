class WordDictionaryNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = WordDictionaryNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = WordDictionaryNode()
            current = current.children[c]
        current.word = True

    def search(self, word: str) -> bool:
        deq = deque([self.root])
        print(word)
        for c in word:
            print(c)
            temp_deq = deq.copy()
            while len(temp_deq) > 0:
                current = temp_deq.popleft()
                deq.popleft()
                print(current.children.keys())

                if c == ".":
                    for _, child in current.children.items():
                        deq.append(child)
                    continue

                if c in current.children:
                    deq.append(current.children[c])
        for last in deq:
            if last.word:
                return True
                
        return False
                
        
