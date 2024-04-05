def is_valid_parentheses(s: str) -> bool:
    """
    在这个实现中，我们遍历输入的字符串s，对于每一个字符：
    如果它是左括号，则将其压入栈中；
    如果它是右括号，则检查栈是否为空以及栈顶元素是否是与其匹配的左括号。如果是，则弹出栈顶元素继续检查；如果不是，则立即返回False，表示括号不匹配。
    最后，如果遍历完整个字符串后栈为空，则说明所有括号都得到了正确匹配，返回True；否则返回False。
    :param s:
    :return:
    """
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map.values():  # 遇到左括号，入栈
            stack.append(char)
        elif char in bracket_map.keys():  # 遇到右括号
            if not stack or stack.pop() != bracket_map[char]:  # 栈非空且栈顶元素不是对应左括号，说明匹配失败
                return False
    return not stack  # 遍历结束后，栈为空说明所有括号都已经匹配成功

if __name__ == '__main__':

    # 示例
    test_string = "([])"
    print(is_valid_parentheses(test_string))  # 输出: True