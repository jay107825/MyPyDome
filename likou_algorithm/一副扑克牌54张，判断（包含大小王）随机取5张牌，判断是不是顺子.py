# 示例：随机生成5张牌（包括大小王）
import random

def is_straight(hand):
    """
    请注意，上述代码示例仅提供了基础逻辑，实际应用中可能需要进一步完善以适应更复杂的情况，
    尤其是大小王如何填补空缺形成顺子的部分。在实际情况中，大小王可能会有多种填补方式
    ，此处简化为只要非零牌可以形成连续序列，且存在足够的大小王填补空缺，就算作顺子。
    在实际编程中，你可能需要更细致地遍历和组合大小王的可能性来判断。
    :param hand:
    :return:
    """
    # 假设hand是一个包含5个整数的列表，0表示大小王
    values = sorted(hand)
    wildcards = values.count(0)  # 统计大小王数量

    # 移除大小王，得到实际点数列表
    non_wild_cards = [value for value in values if value != 0]

    # 对于非零牌进行顺子判断
    if len(non_wild_cards) < 5 - wildcards:  # 如果非零牌不够5张，则不可能构成顺子
        return False

    min_non_zero_card, max_non_zero_card = min(non_wild_cards), max(non_wild_cards)
    non_zero_card_count = max_non_zero_card - min_non_zero_card + 1

    # 没有大小王参与，直接判断非零牌是否连续
    if non_zero_card_count == len(non_wild_cards) and non_zero_card_count == 5 - wildcards:
        return True
    # 有大小王参与，判断去掉大小王后的牌是否连续，并且非零牌之间最大间隔不超过wildcards
    elif non_zero_card_count + wildcards >= 5 and all(
            abs(a - b) <= 1 for a, b in zip(non_wild_cards[:-1], non_wild_cards[1:])):
        return True
    else:
        return False



if __name__ == '__main__':
    deck = list(range(14)) * 4 + [0, 0]  # 52张普通牌 + 2张大小王
    random.shuffle(deck)
    hand = deck[:5]
    print(hand)
    print(is_straight(hand))