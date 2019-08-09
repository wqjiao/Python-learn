# Python 学习笔记

## Python 安装地址

[Windows 不同版本号及操作系统](https://www.python.org/ftp/python/3.7.4/)

## Visual C++ vc_redist.x64.exe 安装

[下载路径](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

## cmder 不同环境命令行支持

方便执行代码

## API

### 运算符

* 算数运算符

|  运算符  |                     描述                      |  实例  |
| :-----: |  :----------------------------------------  | :----: |
|    +    | 加  - 两个对象相加                             |  a + b |
|    -    | 减  - 得到负数或是一个数减去另一个数             |  a - b |
|    *    | 乘  - 两个数相乘或是返回一个被重复若干次的字符串  |  a * b |
|    /    | 除  - x除以y                                   |  a / b |
|    %    | 取模  - 返回除法的余数                          |  a % b |
|    **   | 幂  - 返回x的y次幂                              | a ** b |
|    //   | 取整除  - 返回商的整数部分（向下取整）            | a // b |

* 比较运算符

|  运算符  |                     描述                      |  实例  |
| :-----: |  :------------------------------------------  | :----: |
|   ==	  | 等于 - 比较对象是否相等 |   (a == b) 返回 False.  |
|   !=	  | 不等于 - 比较两个对象是否不相等 |   (a != b) 返回 true. |
|   <>	  | 不等于 - 比较两个对象是否不相等 |	(a <> b) 返回 true。这个运算符类似 != 。|
|   >	  | 大于 - 返回x是否大于y |	(a > b) 返回 False。|
|   <	  | 小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。|	(a < b) 返回 true。|
|   >=	  | 大于等于	- 返回x是否大于等于y。|	(a >= b) 返回 False。|
|   <=	  | 小于等于 -	返回x是否小于等于y。|	(a <= b) 返回 true。|

* 占位运算符

整数向下取整 %d
数值浮点数(默认小数点后6位有效数值) %f

### 变量类型

* 使用 `type()` 检查变量的类型

```Python
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>
```
