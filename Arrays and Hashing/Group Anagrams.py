class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            lst = [0]*26
            for char in word:
                lst[ord(char)-ord("a")] += 1
            dic[tuple(lst)].append(word)
        return dic.values()


