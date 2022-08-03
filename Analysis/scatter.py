import glob
import re

import matplotlib.pylab as plt
import numpy as np
import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/*.txt"

figure, axis = plt.subplots(3, 2)

for file_name in glob.glob(path):
    df = pd.read_csv(file_name, header=None)

    user = re.findall(r'[^\/]+(?=\.)', file_name)

    grouped = df.groupby(df[2])

    # 1
    part_1 = grouped.get_group(1)
    axis[0, 0].scatter(part_1[3], part_1[4], part_1[1]*5, marker='+', alpha=0.6, label=user[0])
    axis[0, 0].set_title("Part 1")
    axis[0, 0].set_yticks(np.arange(1, 5, 1.0))
    axis[0, 0].legend(bbox_to_anchor=(1.13, 0.4))

    # 4
    part_4 = grouped.get_group(4)
    axis[0, 1].scatter(part_4[4], part_4[3], part_4[1]*5, marker='2', alpha=0.6, label=user[0])
    axis[0, 1].set_title("Part 4")
    axis[0, 1].set_xticks(np.arange(1, 5, 1.0))
    axis[0, 1].legend(bbox_to_anchor=(1.13, 0.4))

    # 2
    part_2 = grouped.get_group(2)
    axis[1, 0].scatter(part_2[3], part_2[4], part_2[1]*5, marker='|', alpha=0.6, label=user[0])
    axis[1, 0].set_title("Part 2")
    axis[1, 0].set_yticks(np.arange(1, 5, 1.0))
    axis[1, 0].legend(bbox_to_anchor=(1.13, 0.4))

    # 5
    part_5 = grouped.get_group(5)
    axis[1, 1].scatter(part_5[4], part_5[3], part_5[1]*5, marker='*', alpha=0.6, label=user[0])
    axis[1, 1].set_title("Part 5")
    axis[1, 1].set_xticks(np.arange(1, 5, 1.0))
    axis[1, 1].legend(bbox_to_anchor=(1.13, 0.4))

    # 3
    part_3 = grouped.get_group(3)
    axis[2, 0].scatter(part_3[3], part_3[4], part_3[1]*5, marker='+', alpha=0.6, label=user[0])
    axis[2, 0].set_title("Part 3")
    axis[2, 0].set_yticks(np.arange(1, 5, 1.0))
    axis[2, 0].legend(bbox_to_anchor=(1.13, 0.4))

    # 6
    part_6 = grouped.get_group(6)
    axis[2, 1].scatter(part_6[4], part_6[3], part_6[1]*5, marker='+', alpha=0.6, label=user[0])
    axis[2, 1].set_title("Part 6")
    axis[2, 1].set_xticks(np.arange(1, 5, 1.0))
    axis[2, 1].legend(bbox_to_anchor=(1.13, 0.4))

# figure.legend(bbox_to_anchor=(1.2, 0.6))
plt.show()
