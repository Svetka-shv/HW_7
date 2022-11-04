# Ex 1 Високосний рік
# num = int(input('Year:'))
# if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
#     print('Yes')
# else:
#     print('No')
#
# print('Yes' if num % 4 == 0 and num % 100 or num % 400 == 0 else 'No')

# Ex 2 Альтернативи
# 1-ша
num = int(input('Year:'))
print('Yes' if num % 4 == 0 and num % 100 != 0 or num % 400 == 0 else 'No')

# 2-га
num = int(input('Year:'))
print('Yes' if num % 4 == 0 and not num % 100 == 0 or num % 400 == 0 else 'No')

3-тя
num = int(input('Year:'))
print((num % 4 == 0 and num % 100 != 0) or (num % 400 == 0))


# Ex 3 Три числа
# fizz = int(input('1'))
# buzz = int(input('2'))
# num = int(input('3'))
# for i in range(1, num + 1):
#     if i % fizz == 0 and i % buzz == 0:
#         i = 'FB'
#     elif i % buzz == 0:
#         i = 'B'
#     elif i % fizz == 0:
#         i = 'F'
#     print(i, end = ' ')
#
#
# fizz = int(input('1'))
# buzz = int(input('2'))
# num = int(input('3'))
# for i in range(1, num + 1):
#     temp = '';
#     if i % fizz == 0:
#         temp += 'F'
#     if i % buzz == 0:
#         temp += 'B'
#     if temp == '':
#         temp = i
#     print(temp, end = ' ')
#
#
# fizz = int(input('1'))
# buzz = int(input('2'))
# num = int(input('3'))
# for i in range(1, num + 1):
#     temp = 'F' if i % fizz == 0 else 'B' if i % buzz == 0 else i
#     print('FB' if i % fizz == 0 and  i % buzz == 0 else temp, end = ' ')
#
# fizz = int(input('1'))
# buzz = int(input('2'))
# num = int(input('3'))
# for i in range(1, num + 1):
#     temp = str(i) if i % fizz else 'F'
#     temp = '' if i % fizz and i % buzz == 0 else temp
#     if i % buzz == 0:
#         temp += 'B'
#     print(temp, end=' ')
#
# fizz = int(input('1'))
# buzz = int(input('2'))
# num = int(input('3'))
# for i in range(1, num + 1):
#     temp = str(i) if i % fizz else 'F'
#     temp +=  '' if i % buzz else 'B'
#     print(temp, end = ' ')
"""Hello my frends"""
