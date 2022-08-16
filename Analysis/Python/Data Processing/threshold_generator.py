import glob
import re

import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/Male/25-30-24/*.txt"


def user_demo_map(user):
    gender = "Male"
    age = 25

    if 1 == user:
        gender = "Female"
        age = 25
    elif 8 == user:
        gender = "Female"
        age = 22
    elif 10 == user:
        gender = "Female"
        age = 21
    elif 11 == user:
        gender = "Female"
        age = 22
    elif 15 == user:
        gender = "Female"
        age = 23
    elif 16 == user:
        gender = "Female"
        age = 24
    elif 2 == user:
        gender = "Male"
        age = 27
    elif 3 == user:
        gender = "Male"
        age = 25
    elif 4 == user:
        gender = "Male"
        age = 19
    elif 5 == user:
        gender = "Male"
        age = 25
    elif 6 == user:
        gender = "Male"
        age = 25
    elif 7 == user:
        gender = "Male"
        age = 21
    elif 9 == user:
        gender = "Male"
        age = 27
    elif 12 == user:
        gender = "Male"
        age = 21
    elif 13 == user:
        gender = "Male"
        age = 23
    elif 14 == user:
        gender = "Male"
        age = 23
    elif 17 == user:
        gender = "Male"
        age = 23
    elif 18 == user:
        gender = "Male"
        age = 21
    elif 19 == user:
        gender = "Male"
        age = 25
    elif 20 == user:
        gender = "Male"
        age = 24

    return gender, age


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

    gender, age = user_demo_map(user[0])

    grouped = df.groupby(df[2])

    for part in range(1, 7):
        group = grouped.get_group(part)
        moisture = group[1].iloc[0]
        for sense in range(1, 5):
            minimum, maximum = get_threshold(df, part, sense)
            if minimum > 0:
                if maximum > 0:
                    if maximum >= minimum:
                        temp = pd.DataFrame(
                            {"user": [user[0]], "Gender": [gender], "Age": [age], "part": [part],
                             "moisture": [moisture], "level": [sense], "minimum": [minimum], "maximum": [maximum],
                             "range": [maximum - minimum]})
                        reformat = reformat.append(temp, ignore_index=True)

reformat.to_csv("/Users/jalapatip/Work/HaRVI/ElectroResults/Study/male_25_30.csv", index=False)
