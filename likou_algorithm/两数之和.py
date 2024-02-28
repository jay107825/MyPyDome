class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            pattern_tatget = target - num
            new_index = index + 1
            if pattern_tatget in nums[new_index:]:
                if pattern_tatget != num:
                    return [index, nums.index(pattern_tatget)]
                else:
                    return [index, nums.index(num, new_index)]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

    nums = [3, 2, 4]
    print(Solution().twoSum(nums, 6))

    nums =[3, 3]
    print(Solution().twoSum(nums, 6))