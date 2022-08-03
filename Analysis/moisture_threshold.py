import glob
import re

import matplotlib.pylab as plt
import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/All/*.txt"


def sequence_generator(n):
    return pd.Series(range(0, len(n)))


def get_threshold(df, part, sense):
    group = df.groupby(df[2])
    group = group.get_group(part).reset_index().groupby(4)

    minimum = -10
    maximum = -20

    if sense in group.groups.keys():
        outlier = {sense}
        for id in range(group['index'].first()[sense], group['index'].last()[sense] + 1):
            if df.loc[id][4] != sense:
                outlier.add(df.loc[id][4])

        if 1 == len(outlier):
            minimum = group[3].min()[sense]
            maximum = group[3].max()[sense]

        if 2 == len(outlier):
            exclude = outlier.difference({sense})
            exclude = exclude.pop()
            if exclude < sense:
                maximum = group[3].max()[sense]
                ex_max = group.get_group(exclude)[3].max()
                iter = group.get_group(sense)[3].sort_values(ascending=True)
                for i in iter:
                    if i > ex_max:
                        minimum = i
            else:
                minimum = group[3].min()[sense]
                ex_min = group.get_group(exclude)[3].min()
                iter = group.get_group(sense)[3].sort_values(ascending=False)
                for i in iter:
                    if i < ex_min:
                        maximum = i

    return minimum, maximum


reformat = pd.DataFrame()

for file_name in glob.glob(path):
    df = pd.read_csv(file_name, header=None)

    user = re.findall(r'[^\/]+(?=\.)', file_name)

    grouped = df.groupby(df[2])

    for part in range(1, 7):
        group = grouped.get_group(part)
        moisture = group[1].iloc[0]
        for sense in range(1, 5):
            minimum, maximum = get_threshold(df, part, sense)
            if minimum > 0:
                if maximum > 0:
                    if maximum >= minimum:
                        print("hello")
                        temp = pd.DataFrame(
                            {"user": [user[0]], "moisture": [moisture], "part": [part], "sense": [sense],
                             "minimum": [minimum], "maximum": [maximum]})
                        reformat = reformat.append(temp, ignore_index=True)


print(reformat)


