# """
# 某公司有三种类型的员工 分别是部门经理、程序员和销售员
# 需要设计一个工资结算系统 根据提供的员工信息来计算月薪
# 部门经理的月薪是每月固定15000元
# 程序员的月薪按本月工作时间计算 每小时150元
# 销售员的月薪是1200元的底薪加上销售额5%的提成
# """
# from abc import ABCMeta, abstractmethod


# class Employee(object, metaclass=ABCMeta):
#     """员工"""

#     def __init__(self, name):
#         """
#         初始化方法

#         :param name: 姓名
#         """
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @abstractmethod
#     def get_salary(self):
#         """
#         获得月薪

#         :return: 月薪
#         """
#         pass


# class Manager(Employee):
#     """部门经理"""

#     def get_salary(self):
#         return 15000.0


# class Programmer(Employee):
#     """程序员"""

#     def __init__(self, name, working_hour=0):
#         super().__init__(name)
#         self._working_hour = working_hour

#     @property
#     def working_hour(self):
#         return self._working_hour

#     @working_hour.setter
#     def working_hour(self, working_hour):
#         self._working_hour = working_hour if working_hour > 0 else 0

#     def get_salary(self):
#         return 150.0 * self._working_hour


# class Salesman(Employee):
#     """销售员"""

#     def __init__(self, name, sales=0):
#         super().__init__(name)
#         self._sales = sales

#     @property
#     def sales(self):
#         return self._sales

#     @sales.setter
#     def sales(self, sales):
#         self._sales = sales if sales > 0 else 0

#     def get_salary(self):
#         return 1200.0 + self._sales * 0.05


# def main():
#     emps = [
#         Manager('刘备'), Programmer('诸葛亮'),
#         Manager('曹操'), Salesman('荀彧'),
#         Salesman('吕布'), Programmer('张辽'),
#         Programmer('赵云')
#     ]
#     for emp in emps:
#         if isinstance(emp, Programmer):
#             emp.working_hour = int(input('请输入%s本月工作时长: ' % emp.name))
#         elif isinstance(emp, Salesman):
#             emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
#         # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
#         print('%s本月工资为: ￥%s元' %
#               (emp.name, emp.get_salary()))


# if __name__ == '__main__':
#     main()

# import tkinter
# import tkinter.messagebox


# def main():
#     flag = True

#     # 修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello, world!')\
#             if flag else ('blue', 'Goodbye, world!')
#         label.config(text=msg, fg=color)

#     # 确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
#             top.quit()

#     # 创建顶层窗口
#     top = tkinter.Tk()
#     # 设置窗口大小
#     top.geometry('240x160')
#     # 设置窗口标题
#     top.title('小游戏')
#     # 创建标签对象并添加到顶层窗口
#     label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
#     label.pack(expand=1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()


# if __name__ == '__main__':
#     main()

"""
使用 pygame 开发小游戏
"""
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """颜色"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
        (self.x, self.y), self.radius, 0)

def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)
             
if __name__ == '__main__':
    main()
