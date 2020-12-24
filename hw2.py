def equals(list):
    brek = [list[a +1]-list[a] for a in range(len(list)-1)]
    return len(set(brek)) == 1

def apply(list, pasos):
    if pasos > 0:
        list = list[pasos:] + list[:pasos]
        return list
    else: 
        list = (list[pasos *-1:] + list[:pasos*-1])[::-1]
        return list

def point (list_, list1):
    point_ = list(filter(lambda y:y in list_, list1))
    return point_

array = [1,1,1,1,2,2,3,4,5,6,7,7,8]
a = [1,2,3,4,5,6]
        
print(apply(array, -5)) 
