# Python实现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_nth_from_end(head, n):
    """
    设置两个指针，快指针 fast 先行 n 步。
    然后快慢指针一起移动，当快指针到达链表末尾时，慢指针所在的位置就是倒数第 n 个节点的前一个节点。
    通过慢指针删除其后继节点（即倒数第 n 个节点）。
    :param head:
    :param n:
    :return:
    """
    if head is None or n <= 0:
        return head

    dummy = ListNode(0, head)  # 创建哑节点便于处理边界条件
    slow = dummy
    fast = dummy

    # 快指针先走n步
    for _ in range(n):
        if fast.next is not None:
            fast = fast.next
        else:
            # 如果n大于链表长度，无需删除任何节点
            return dummy.next

    # 同时移动快慢指针，直到快指针到达链表末尾
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # 删除慢指针指向的下一个节点（即倒数第n个节点）
    slow.next = slow.next.next

    return dummy.next  # 返回新的头节点