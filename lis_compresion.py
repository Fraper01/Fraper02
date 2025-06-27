# lis compresion vamos a ver de que va esto
# nos permite con lista mas potentes

my_list_original = list()
my_list_original = [35,24,62,52,30,30,17]
my_list_original = [0,1,2,3,4,5,6,7]
my_list = [i for i in my_list_original]
print(my_list)
my_list = [i for i in range(8)]
print(my_list)
my_list = [i+1 for i in range(8)] # crea lista con lo que tu quieras en general valores en vez de ir con append o insert
print(my_list)
my_list = [i*i for i in range(8)] # crea lista con lo que tu quieras en general valores en vez de ir con append o insert
print(my_list)

def sum_five(number):
    return number+5

my_list = [sum_five(i) for i in range(8)] # crea lista con lo que tu quieras en general valores en vez de ir con append o insert
print(my_list)

