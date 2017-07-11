import os
import psutil
import random
import time


names = ['한민수', '김김김', '지지지', '박박박', '최최최', '성성성']
majors = ['컴퓨터공학', '멀티미디어학', '간호학', '영문학', '경영학', '화학공학']

process = psutil.Process(os.getpid())
mem_before =  process.memory_info().rss / 1024 / 1024


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                'id' : i,
                'name' : random.choice(names),
                'major' : random.choice(majors),
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                'id' : i,
                'name' : random.choice(names),
                'major': random.choice(majors),
                }
        yield person

t1 = time.clock()
people = people_generator(100000000)
t2 = time.clock()
mem_after = process.memory_info().rss / 1024 / 1024
total_time = t2 - t1

print('시작 전 메모리 사용량 : {} MB'.format(mem_before))
print('종료 후 메모리 사용량 : {} MB'.format(mem_after))
print('총 소요된 시간: {:.6f}초'.format(total_time))
