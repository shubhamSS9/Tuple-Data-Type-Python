# a = "shubham", 25, 28.0, 74674847877743

# print(a)
# print(type(a))
# print((a,)*5)
# print(10*5)

# tpl = ("Handle", "Exception", "Like", "a", "boss")
# print(tpl)
# print(tpl[1],tpl[4])

# tpl = ("shubham", 30, 50, 87.98, 100)
# print(max(tpl))

# tpl[0] = "Susha"
# print(tpl)

# i = 0
# while i < len(tpl):
#     print(tpl[i])
#     i=i+1

# for i in tpl:
#     print(i)

# for i, ele in enumerate(tpl):
#     print(i, ele)

# t = (12, 15, 13, 23, 22, 16, 17)
# print(len(t))
# print(max(t))
# print(sum(t))
# print(any(t))
# print(sorted(t))

# print(t.count(15))

# t1 = (2, 4, 5, 3, 6, 6, 9)
# t2 = (5, 8, 2, 7, 5, 4, 1)
# c = (t1, t2)
# print(c[0][6],c[1][6])

# records = (
#     ("Priyanka", 24, 3455.50), ("Shailesh", 25, 4555.50),
#     ("Subhash", 25, 4505.50), ("Sugandha", 27, 4455.55)
#     )


# print(records[0][0], records[0][1], records[0][2])
# print(records[1][0], records[1][1], records[1][2])

# print(records[0][0], records[1][0], records[2][0])
# print(records[3][0], records[0][0], records[0][0])


# for n, a, s in records:
#     print(n,a)

# x = (6, 4, 7, 8, 9)
# y = (5, 8, 1, 2, x, 5)
# print(y)

# x = (6, 4, 7, 8, 9)
# y = (5, 8, 1, 2, *x, 5)
# print(y)

# import operator

# lst = [("Sriyanka", 24, 9455.50), ("Phailesh", 25, 4555.50)]
# tpl = (["Sriyanka", 24, 3455.50], ["Phailesh", 25, 4555.50])

# # print(sorted(lst))
# # print(sorted(tpl))

# print(sorted(lst, key=operator.itemgetter(2)))
# print(sorted(tpl, key=operator.itemgetter(2)))

# result = divmod(10, 2)
# print(result)

# s = (12, 2)
# print(divmod(*s))