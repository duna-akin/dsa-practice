class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPI = 0
        rightPI = len(numbers) - 1

        while leftPI < rightPI:
            if numbers[leftPI] + numbers[rightPI] > target:
                rightPI -= 1

            elif numbers[leftPI] + numbers[rightPI] < target:
                leftPI += 1

            else:
                break
            
        return [leftPI + 1, rightPI + 1]