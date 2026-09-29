class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            diff = target - numbers[i]

            if diff not in numbers:
                i +=1 
            else:
                if diff == numbers[j]:
                    return [i+1, j+1]
                j -= 1