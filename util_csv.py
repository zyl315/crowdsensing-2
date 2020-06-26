import csv
import random
from itertools import islice


def create_csv(name, csv_head):
    path = 'csv_file/' + name + '.csv'
    with open(path, 'w') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(csv_head)


def read_csv(name):
    path = 'csv_file/' + name + '.csv'
    res = []
    with open(path, "r") as f:
        csv_read = csv.reader(f)
        for p in islice(csv_read, 1, None):
            tmp = map(float, p)
            res.append(list(tmp))

    return res
    # for line in csv_read:
    #     print(line)


def write_csv(name, data_row):
    path = 'csv_file/' + name + '.csv'
    with open(path, 'a', newline="") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)


if __name__ == '__main__':
    # create_csv('test', ['a', 'b'])
    # write_csv('test')
    # for i in range(200):
    #     x = round(random.uniform(41.875750, 41.887780), 6)
    #     y = round(random.uniform(-87.636954, -87.616353), 6)
    #     write_csv('Point', [i, x, y])

    # for i in range(80):
    #     x = random.randint(0, 100)
    #     y = random.randint(0, 100)
    #     write_csv('User', [i, x, y, 0.5])

    # create_csv('result1', ['node_id', 'rate', 'budget_save', 'user_num'])
    # create_csv('result2', ['node_id', 'rate', 'budget_save', 'user_num'])
    # create_csv('result3', ['node_id', 'rate', 'budget_save', 'user_num'])
    # create_csv('test', ['node_id', 'rate', 'budget_save', 'user_num'])
    write_csv('test', ['1', '2', '3', '4'])
    pass
