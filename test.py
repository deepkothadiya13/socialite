# import requests
# print("hello")
# link = "https://www.linkedin.com/feed/"
# html = requests.get(link, params=None)
# print(html.text)
# print(type(html))
# import array as arr
#
# my_array = arr.array('i', [1,2,3])
# print(my_array[::-1])
#
# from random import shuffle
# x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
# shuffle(x)
# print(x)
#
# import random
# print(random.normalvariate(0,9))
#
# cap = "hello world"
# trail= cap.split()
# for i in range(len(trail)):
#     print(trail[i].capitalize())
#
# match = [1,1,3,4,5,67]
#
# match.remove(5)
# print(match)

count = []
trail = "aabbbd"
tr=trail.strip()
str_list = trail.split()
print(tr[0])
for i in tr:
    print(i)
    if i in trail:
        count.append(trail.count(i))

print(max(count))