class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)
        for word in strs:
            alphabet_counter = [0] * 26
            for c in word:
                alphabet_counter[ord(c) - ord('a')] += 1
            anagram_list[tuple(alphabet_counter)].append(word)
        return [i for i in anagram_list.values()]