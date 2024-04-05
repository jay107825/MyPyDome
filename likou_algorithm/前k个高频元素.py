import collections
import heapq


def top_k_frequent(nums, k):
    """
    这个函数首先使用collections.Counter统计输入列表nums中每个元素的频率，
    然后创建一个包含频率和对应数字的元组列表。接着调用heapq.nlargest函数，
    传入参数k和一个key函数（在这里是对频率取负数以实现降序排序）
    。最后，从结果中提取出数字并返回。这个解决方案的时间复杂度接近O(N log K)。
    :param nums:
    :param k:
    :return:
    """
    # Step 1: Count the frequency of each number
    count_dict = collections.Counter(nums)

    # Step 2: Create a list of (frequency, number) tuples
    count_pairs = [(freq, num) for num, freq in count_dict.items()]

    # Step 3: Use heapq.nlargest to get the top k frequent elements
    # Note that we use -freq as the first element in the tuple to sort by descending order
    top_k = heapq.nlargest(k, count_pairs, key=lambda x: -x[0])

    # Return only the numbers (without their frequencies)
    return [pair[1] for pair in top_k]


if __name__ == '__main__':
    # 示例
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(result)  # 输出: [1, 2]
