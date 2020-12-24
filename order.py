dbase = [
    '+5(4671)849-6225',
    '+394(63)128-1148',
    '535(02)715-68-89',
    '+72(23)661-8520',
    '+194(455)628-2961',
    '092158146777',
    '+862(179)416-6138',
    '+3(2697)794-4711',
    '+98(393)874-4458',
    '+3(632)626-8042',
    '+7611528-9013',
    '+88135130-7172',
    '94(3005)670-58-48',
    '+264925558-7301',
    '58(6929)091-8491',
    '+581(067)254-6659',
    '+4(838)997-1720',
    '+7(163)228-1948',
    '72236618520',
    '967(28)959-4951',
    '+53(2121)207-3793',
    '+80(922)2856718',
    '7121-2173999'
]
numbers = []
codes_a = []
codes_c = []
codes_u = []

new_list = [a.replace("+", "").replace("-", "").replace("(", "").replace(")",  "") for a in dbase]

for i in new_list:
    numbers.append((i[:2], i[2:5], i[5:]))
    codes_a.append(i[2:5])
    codes_c.append(i[:2])
    codes_u.append(i[5:])

max_num = max(new_list, key=len)
print(numbers) #first task
print('In the database there are', len(set(new_list)), ' phone numbers.') #second task
print('In the database there are', len(set(codes_c)), ' countries.') #third task
print('The biggest number is', max_num) #fourth task

R_numbers = []
sin_pathern = set(new_list)  #organize the non-pathern numbers, fifth task
for i in sin_pathern:
    if int(i[0]) == 7:
        R_numbers.append(i)
print('The russians numbers are:' , R_numbers) # sixth task


