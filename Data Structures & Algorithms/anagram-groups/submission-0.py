class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {"".join(sorted(strs[0])): [strs[0]]}

        for i in range(1, len(strs)):
            if "".join(sorted(strs[i])) in groups:
                # append the word to the list that corresponds to that key
                groups.get("".join(sorted(strs[i]))).append(strs[i])
            else:
                groups["".join(sorted(strs[i]))] = [strs[i]]

        return list(groups.values())