from multiprocessing import Pool


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def finder(file_name):
    for line in read_file(file_name):
        if line == 'a\n':
            return True
    return False

file_list = ['aa.txt', 'bb.txt', 'cc.txt']

if __name__ == '__main__':
    pool = Pool(processes=1)
    result_list = list(pool.map(finder, file_list))

    print(result_list)
