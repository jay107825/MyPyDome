# @ProjectName:MyPyDome
# @Autor:柴志杰
# @Date:2024/8/4:下午4:44
# @FileName: Conversion
# @alias: jay_Conversion
# @module_name:  将十进制数转换成25进制


def decimal_to_base25(n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWX"
    if n == 0:
        return '0'
    result = ''
    while n:
        result = digits[n % 25] + result
        n //= 25
    return result

if __name__ == '__main__':

    # 测试函数
    tests = [0, 1, 24, 25, 59, 60, 624, 625, 15624, 15625, 1000000]
    for test in tests:
        print(f"Decimal {test} in Base 25 is: {decimal_to_base25(test)}")