from multiprocessing import Pool

import time


start_time = time.time()

def logfinder(n):
    for i in range(n):
        if 100000000 == i:
            return 1
    return 0


value = [100000000, 100000000, 100000000, 100000001]


#result_list = []
#
#for i in value:
#    result = logfinder(i)
#    result_list.append(result)
#print(time.time() - start_time)
#print(result_list)

pool = Pool(processes=4)

def change_bool(aa):
    if aa == 1:
        return True
    return False

print(list(map(change_bool, pool.map(logfinder, value))))
print(time.time()-start_time)
