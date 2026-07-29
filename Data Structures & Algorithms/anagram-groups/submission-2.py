class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {"".join(sorted(strs[0])): [strs[0]]}

        for i in range(1, len(strs)):
            sortedString = "".join(sorted(strs[i]))

            if sortedString in groups:
                groups.get(sortedString).append(strs[i])

            else:
                groups[sortedString] = [strs[i]]

        return list(groups.values())