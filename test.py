import csv
import pprint

print('hellow world')


with open('./sample.csv') as f:
    # print(f.read())

    reader = csv.reader(f)
#    for row in reader:
#       print(row)

    l = [row for row in reader]
    print(l)

    print(l[1])

    print(l[1][1])

    print(type(l[1][1]))

    l_T = [list(x) for x in zip(*l)]
    print(l_T)

import numpy as np
import pandas as pd