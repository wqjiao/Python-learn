# print('hello world')


# def main():
    # f = None
    # try:
    #     f = open('致橡树.txt', 'r', encoding='utf-8')
    #     print(f.read())
    # except FileNotFoundError:
    #     print('无法打开指定的文件!')
    # except LookupError:
    #     print('指定了未知的编码!')
    # except UnicodeDecodeError:
    #     print('读取文件时解码错误!')
    # finally:
    #     if f:
    #         f.close()

    # try:
    #     with open('致橡树.txt', 'r', encoding='utf-8') as f:
    #         print(f.read())
    # except FileNotFoundError:
    #     print('无法打开指定的文件!')
    # except LookupError:
    #     print('指定了未知的编码!')
    # except UnicodeDecodeError:
    #     print('读取文件时解码错误!')


# import time

# def main():
#     # 一次性读取整个文件内容
#     with open('致橡树.txt', 'r', encoding='utf-8') as f:
#         print(f.read())

#     # 通过for-in循环逐行读取
#     with open('致橡树.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()

#     # 读取文件按行读取到列表中
#     with open('致橡树.txt') as f:
#         lines = f.readlines()
#     print(lines)

# if __name__ == '__main__':
#     main()


# 装饰器
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
