# Ex_1
# str_1, str_2, str_3 = input(), input(), input()
# temp_1 = str_1[len(str_1) // 2] if len(str_1) % 2 else str_1[len(str_1) // 2-1:len(str_1) // 2 +1]
# temp_2 = str_2[len(str_2) // 2] if len(str_2) % 2 else str_2[len(str_2) // 2-1:len(str_2) // 2 +1]
# temp_3 = str_3[len(str_3) // 2] if len(str_3) % 2 else str_3[len(str_3) // 2-1:len(str_3) // 2 +1]
# print(temp_1)
# print(temp_2)
# print(temp_3)

"""Через функцію"""
# def average(symbol):
#     temp = symbol[len(symbol) // 2] if len(symbol) % 2 else symbol[len(symbol) // 2-1:len(symbol) // 2 +1]
#     return temp
#
# print(average(input()))
# print(average(input()))
# print(average(input()))




# # Ex_2
# str_1 = input('Input string: ')
# if 5 <= len(str_1) <= 15:
#     start = str_1[len(str_1) // 2:]
#     end = str_1[:len(str_1) // 2 - 3]
#     end_upper = str_1[len(str_1) // 2 -3:len(str_1) // 2].upper()
#     print(start + end + end_upper)
# else:
#     print(False)


# # Ex_3
# str_1 = input('Input string: ').upper()
# if len(str_1) <= 10:
#     str_upper = str_1[:-3]
#     start = str_upper[:len(str_upper) // 2]
#     end = str_upper[len(str_upper) // 2:]
#     str_lower = str_1[-3:].lower()
#     print(start + str_lower + end)

# # Ex_4
# square = int(input())
# for i in range(square):
#     for j in range(square):
#         if j == 0 or i ==  0 or i == square - 1 or j == square -1 :
#             print("#", end='')
#         else:
#             print(" ", end='')
#     print("")