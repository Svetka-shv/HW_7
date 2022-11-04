# Ex_1
# list_1 = [1, 56, 2, 12, 9000, 23, 6, 343, 69, 4, 777]
# a---------------------------
# for i in range(len(list_1)):
#     if i % 2 == 0:
#         print(list_1[i], end=' ')
#
# print(*[list_1[i] for i in range(len(list_1)) if i % 2 == 0 ], end=' ')

# print(*list_1[::2])


# b----------------------------
# count = 0
# for i in range(len(list_1)):
#     count += list_1[i]
# print(count)
# print([count for i in range(len(list_1))  count += list_1[i] ])
# c--------------------------------
# count_even = 0
# count_not_even = 0
# for i in range(len(list_1)):
#     if i % 2 == 0:
#         count_even += list_1[i]
#     else:
#         count_not_even += list_1[i]
# print(count_even)
# print(count_not_even)

# d-------------------------------------
# bigest_num = 0
# for i in range(len(list_1)):
#     if list_1[i] > bigest_num:
#         bigest_num = list_1[i]
# print(bigest_num, list_1.index(bigest_num))

# Ex_2
# fl = open('file_1.txt', 'r')
# for i in range(10):
#     num = fl.readline().split()
#     for j in range(1, int(num[2]) + 1):
#         temp = str(j) if j % int(num[0]) else 'F'
#         temp = '' if j % int(num[0]) and j % int(num[1]) == 0 else temp
#         if j % int(num[1]) == 0:
#             temp += 'B'
#         print(temp, end=' ')
#     print()
# fl.close()


# Ex_3 для заданого списку
# list = [32,43,1,3,4,5,34,5,1,7,10,34,17,11,15,2,45,90,33,9]
# list_1 = list[:5]
# list_1.sort()
# list_2 = list[5:10]
# list_2.sort(reverse = True)
# list_3 = list[10:15]
# list_3.sort()
# list_4 = list[15:20]
# list_4.sort(reverse = True)
# list_fin = []
# list_fin.extend(list_1)
# list_fin.extend(list_2)
# list_fin.extend(list_3)
# list_fin.extend(list_4)
# print(list_fin)

# Ex_3 для будь-якого списку, який потрібно вводити
# n = int(input())
# list= []
# for i in range(n):
#     num = int(input())
#     list.append(num)
# list_fin = []
# list_1 = []
# list_2 = []
# for j in range(len(list)):
#     if list[:5]:
#         list_1 = list[:5]
#         list_1.sort()
#         list_fin.extend(list_1)
#         if list[5:10]:
#             list_2 = list[5:10]
#             list_2.sort(reverse=True)
#             list_fin.extend(list_2)
#         del list[0:10]
#         continue
# print(list_fin)

# Ex_3 для будь-якого списку, який потрібно вводити
# n = int(input())
# list = []
# for i in range(n):
#     num = int(input())
#     list.append(num)
# for j in range(0, len(list), 5):
#     list[j:j+5] = sorted(list[j:j+5], reverse= j % 2)
#     print(j)
# print(list)


