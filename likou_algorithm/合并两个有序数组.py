def merge_sorted_arrays(arr1, arr2):
    # 初始化两个指针分别指向两个数组的起始位置
    i = j = 0
    # 初始化一个空的结果数组用来存放合并后的有序数组
    result = []

    # 当至少有一个数组还有剩余元素时进行循环
    while i < len(arr1) and j < len(arr2):
        # 将较小的元素添加到结果数组中，并将对应的指针向前移动一位
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # 若第一个数组还有剩余元素，则将其全部添加到结果数组中
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    # 若第二个数组还有剩余元素，则将其全部添加到结果数组
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result
if __name__ == '__main__':

    # 示例
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    merged_arr = merge_sorted_arrays(arr1, arr2)
    print(merged_arr)  # 输出：[1, 2, 3, 4, 5, 6, 7, 8]