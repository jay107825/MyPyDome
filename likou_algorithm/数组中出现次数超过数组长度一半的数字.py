def majorityElement(nums):
    """
    每次遍历时，计数值count代表当前候选数字领先其他数字的数量。当遇到一个与候选数字不同的新数字时，count减1；
    若遇到与候选数字相同的数字时，count加1。若count为0，则更换候选数字。
    遍历完成后，候选数字即为可能的多数元素，再通过计数确认其是否真正出现了超过一半的次数
    :param nums:
    :return:
    """
    if not nums:
        return None

    count = 0
    candidate = nums[0]

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # 检查候选数字是否真的出现了超过一半的次数
    return candidate if nums.count(candidate) > len(nums) // 2 else None


if __name__ == '__main__':
    # 示例
    nums = [3, 2, 3, 2, 2]
    majority_num = majorityElement(nums)
    print(majority_num)  # 输出: 3
