a = [1,2,3,4,5,6]

def task(a, **args):
    array_s = args.get('SUMA', None)
    raiz = args.get('RAIZ', None)
    final_array = args.get('ABSOLUTE', None)
    
    cuadrado_r = [(abs(i) ** 0.5) for i in a]
    a_array = [abs(i) for i in a]

    if array_s:
        return sum(a)
    if final_array:
        return  a_array
    if raiz:
        return cuadrado_r
    if array_s and raiz:
        return cuadrado_r
    if array_s and raiz and final_array:
        return sum(cuadrado_r)

print(task(a, sum=True, root=True, absolute=True, ))
