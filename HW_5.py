"""Ex_1"""
# def idx_sort(list, start_sort, end_sort):
#     list[start_sort:end_sort] = sorted(list[start_sort:end_sort])
#     return print(list)
#
#
# n = int(input("Розмір списку: "))
# list = []
# for i in range(n):
#     num = int(input("Дані списку: "))
#     list.append(num)
# start_sort = int(input("Індекс початку: "))
# end_sort = int(input("Індекс кінця: "))
#
# idx_sort(list, start_sort, end_sort)


"""Ex_2"""
# with open('file_2.txt', 'r+', encoding="UTF-8") as fl:
#     count_line = len(open('file_2.txt').readlines())
#     cond = open('file_2.txt').readlines()
#     def result():
#         list = []
#         for i in range(count_line):
#             try:
#                 a = fl.readline()
#                 list.append(eval(a))
#             except ZeroDivisionError:
#                 list.append('На нуль ділити не можна')
#         return list
#     resul = result()
# with open('file_2.txt', mode ='w+', encoding="UTF-8") as fl:
#     for i in range(count_line):
#         w = ''.join((str(j) for j in cond[i:i+1])).strip()
#         e = ''.join((str(x) for x in resul[i:i+1]))
#         fl.write(w + ' = ' + e + '\n')
# fl.close()

"""Ex_3"""
# def is_palindrome(text):
#     list = []
#     for el in text:
#         if el.isalpha():
#             list.append(el.lower())
#     if list[:] == list[::-1]:
#         return 'Паліндром'
#     else:
#         return 'Ні'
#
# text = input("Input palindrome: ")
# print(is_palindrome(text))