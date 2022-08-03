import glob
import re

import matplotlib.pylab as plt
import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/*.txt"

figure, axis = plt.subplots(3, 2)

for file_name in glob.glob(path):
    df = pd.read_csv(file_name, header=None)

    user = re.findall(r'[^\/]+(?=\.)', file_name)
    print(user[0])

    df[5] = user[0]

    # grouped = df.groupby([df[2], df[4]])
    # print(f'######## {user[0]} ########')
    # print(grouped.head(1))
    # print('#######')
    # print(grouped.get_group((1, 2)))
    # print('\n')

    grouped = df.groupby([df[2], df[4]])

    # 1
    r_1 = grouped.get_group((1, 1))
    axis[0, 0].scatter(r_1[5], r_1[3], 200, marker='^', alpha=0.4, label='1')
    r_2 = grouped.get_group((1, 2))
    axis[0, 0].scatter(r_1[5], r_1[3], 200, marker='>', alpha=0.4, label='2')
    r_3 = grouped.get_group((1, 3))
    axis[0, 0].scatter(r_1[5], r_1[3], 200, marker='v', alpha=0.4, label='3')
    r_4 = grouped.get_group((1, 4))
    axis[0, 0].scatter(r_1[5], r_1[3], 200, marker='<', alpha=0.4, label='4')
    axis[0, 0].set_title("Part 1")
    axis[0, 0].legend(bbox_to_anchor=(1.13, 0.4))

    # 4
    r_1 = grouped.get_group((4, 1))
    axis[0, 1].scatter(r_1[5], r_1[3], 200, marker='^', alpha=0.4, label='1')
    r_2 = grouped.get_group((4, 2))
    axis[0, 1].scatter(r_1[5], r_1[3], 200, marker='>', alpha=0.4, label='2')
    r_3 = grouped.get_group((4, 3))
    axis[0, 1].scatter(r_1[5], r_1[3], 200, marker='v', alpha=0.4, label='3')
    r_4 = grouped.get_group((4, 4))
    axis[0, 1].scatter(r_1[5], r_1[3], 200, marker='<', alpha=0.4, label='4')
    axis[0, 1].set_title("Part 4")
    axis[0, 1].legend(bbox_to_anchor=(1.13, 0.4))

    # 2
    r_1 = grouped.get_group((2, 1))
    axis[1, 0].scatter(r_1[5], r_1[3], 200, marker='^', alpha=0.4, label='1')
    r_2 = grouped.get_group((2, 2))
    axis[1, 0].scatter(r_1[5], r_1[3], 200, marker='>', alpha=0.4, label='2')
    r_3 = grouped.get_group((2, 3))
    axis[1, 0].scatter(r_1[5], r_1[3], 200, marker='v', alpha=0.4, label='3')
    r_4 = grouped.get_group((2, 4))
    axis[1, 0].scatter(r_1[5], r_1[3], 200, marker='<', alpha=0.4, label='4')
    axis[1, 0].set_title("Part 2")
    axis[1, 0].legend(bbox_to_anchor=(1.13, 0.4))

    # 5
    r_1 = grouped.get_group((5, 1))
    axis[1, 1].scatter(r_1[5], r_1[3], 200, marker='^', alpha=0.4, label='1')
    r_2 = grouped.get_group((5, 2))
    axis[1, 1].scatter(r_1[5], r_1[3], 200, marker='>', alpha=0.4, label='2')
    r_3 = grouped.get_group((5, 3))
    axis[1, 1].scatter(r_1[5], r_1[3], 200, marker='v', alpha=0.4, label='3')
    r_4 = grouped.get_group((5, 4))
    axis[1, 1].scatter(r_1[5], r_1[3], 200, marker='<', alpha=0.4, label='4')
    axis[1, 1].set_title("Part 5")
    axis[1, 1].legend(bbox_to_anchor=(1.13, 0.4))

    # 3
    r_1 = grouped.get_group((5, 1))
    axis[2, 0].scatter(r_1[5], r_1[3], 200, marker='^', alpha=0.4, label='1')
    r_2 = grouped.get_group((5, 2))
    axis[2, 0].scatter(r_1[5], r_1[3], 200, marker='>', alpha=0.4, label='2')
    r_3 = grouped.get_group((5, 3))
    axis[2, 0].scatter(r_1[5], r_1[3], 200, marker='v', alpha=0.4, label='3')
    r_4 = grouped.get_group((5, 4))
    axis[2, 0].scatter(r_1[5], r_1[3], 200, marker='<', alpha=0.4, label='4')
    axis[2, 0].set_title("Part 3")
    axis[2, 0].legend(bbox_to_anchor=(1.13, 0.4))

    # 6
    r_1 = grouped.get_group((6, 1))
    axis[2, 1].scatter(r_1[5], r_1[3], 100, marker='s', alpha=0.4, label='1')
    r_2 = grouped.get_group((6, 2))
    axis[2, 1].scatter(r_1[5], r_1[3], 200, marker='s', alpha=0.4, label='2')
    r_3 = grouped.get_group((6, 3))
    axis[2, 1].scatter(r_1[5], r_1[3], 300, marker='s', alpha=0.4, label='3')
    r_4 = grouped.get_group((6, 4))
    axis[2, 1].scatter(r_1[5], r_1[3], 400, marker='s', alpha=0.4, label='4')
    axis[2, 1].set_title("Part 6")
    axis[2, 1].legend(bbox_to_anchor=(1.13, 0.4))

plt.show()