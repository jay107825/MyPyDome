class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

def demo():
    # 使用
    singleton = Singleton()
    another_singleton = Singleton()
    if singleton is another_singleton:  # 两次获取的对象是同一个对象
        return True
    else:
        return False

if __name__ == '__main__':
    print(demo())
