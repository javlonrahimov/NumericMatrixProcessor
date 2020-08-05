int_list = [int(x) for x in input()]
# print([sum((int_list[0:int_list.index(x) + 1])) for x in int_list])
sum_list = []
sum_ = 0
for i in int_list:
    sum_ += i
    sum_list.append(sum_)
print(sum_list)
