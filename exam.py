
def made_list(*argc):
    return [str(a).replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '') for a in argc]  #number 1

def made_list0(list_to_merge):
    list_to_merge =  [[1, 8, 3], [-5, 0], [4], [2, 3, 3]]
    return [e for new_list in list_to_merge for e in new_list]      #number 2

pows = (1/3, 7, 10, -2, -7)
numbers = (3, 2, 0, -2, -7)
make_pow = list(map(lambda a, b: a ** b, numbers, pows))  #number 3

list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
make_list = set(tuple(a) for a in list_of_lists)  #number 4

def extend(list, index = 2, lim =[99,0]):
    list = ([1,2], [3,4], [5,6])
    return [list[index] + lim if index_ == index else a for index_, a in enumerate(list)]
    print(extend(list))




