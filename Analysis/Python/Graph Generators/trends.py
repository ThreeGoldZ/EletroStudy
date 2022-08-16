import glob
import re

import matplotlib.pylab as plt
import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/All/3.txt"


def sequence_generator(n):
    return pd.Series(range(0, len(n)))


figure, axis = plt.subplots(3, 2)

colors = {1: 'gray', 2: 'orange', 3: 'green', 4: 'red'}

for file_name in glob.glob(path):
    df = pd.read_csv(file_name, header=None)

    user = re.findall(r'[^\/]+(?=\.)', file_name)

    grouped = df.groupby(df[2])

    # 1
    part = grouped.get_group(1)
    x = sequence_generator(part)
    axis[0, 0].plot(x, part[3], label=user[0])
    axis[0, 0].scatter(x, part[3], c=part[4].map(colors), marker='^', alpha=0.6, zorder=3)
    # axis[0, 0].legend(bbox_to_anchor=(1.13, 0.4))
    axis[0, 0].set_title("Part 1")

    # 4
    part = grouped.get_group(4)
    x = sequence_generator(part)
    axis[0, 1].plot(x, part[3], label=user[0])
    axis[0, 1].scatter(x, part[3], c=part[4].map(colors), marker='^', alpha=0.6, zorder=3)
    # axis[0, 1].legend(bbox_to_anchor=(1.13, 0.4))
    axis[0, 1].set_title("Part 4")

    # 2
    part = grouped.get_group(2)
    x = sequence_generator(part)
    axis[1, 0].plot(x, part[3], label=user[0])
    axis[1, 0].scatter(x, part[3], c=part[4].map(colors), marker='^', alpha=0.6, zorder=3)
    # axis[1, 0].legend(bbox_to_anchor=(1.13, 0.4))
    axis[1, 0].set_title("Part 2")

    # 5
    part = grouped.get_group(5)
    x = sequence_generator(part)
    axis[1, 1].plot(x, part[3], label=user[0])
    axis[1, 1].scatter(x, part[3], c=part[4].map(colors), marker='^', alpha=0.6, zorder=3)
    # axis[1, 1].legend(bbox_to_anchor=(1.13, 0.4))
    axis[1, 1].set_title("Part 5")

    # 3
    part = grouped.get_group(3)
    x = sequence_generator(part)
    axis[2, 0].plot(x, part[3], label=user[0])
    axis[2, 0].scatter(x, part[3], c=part[4].map(colors), marker='^', alpha=0.6, zorder=3)
    # axis[2, 0].legend(bbox_to_anchor=(1.13, 0.4))
    axis[2, 0].set_title("Part 3")

    # 6
    part = grouped.get_group(6)
    x = sequence_generator(part)
    axis[2, 1].plot(x, part[3], label=user[0])
    axis[2, 1].scatter(x, part[3], c=part[4].map(colors), marker='^', alpha=0.6, zorder=3)
    # axis[2, 1].legend(bbox_to_anchor=(1.13, 0.4))
    axis[2, 1].set_title("Part 6")

    axis[0, 0].legend(bbox_to_anchor=(1.14, 1.2))
    axis[0, 1].legend(bbox_to_anchor=(1.14, 1.2))
    axis[1, 0].legend(bbox_to_anchor=(1.14, 1.25))
    axis[1, 1].legend(bbox_to_anchor=(1.14, 1.25))
    axis[2, 0].legend(bbox_to_anchor=(1.14, 1.0))
    axis[2, 1].legend(bbox_to_anchor=(1.14, 1.0))

figure.legend(bbox_to_anchor=(1.13, 0.4))
# figure.suptitle('Male 19-24', fontsize=20)
# plt.savefig("/Users/jalapatip/Desktop/Graphs/Trends_Modified/17.png")
plt.show()
