import glob
import re
import statistics as stats
import warnings

import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/All/*.txt"


def user_demo_map(user):
    gender = "Male"
    age = 25

    if 1 == int(user):
        gender = "Female"
        age = 25
    elif 8 == int(user):
        gender = "Female"
        age = 22
    elif 10 == int(user):
        gender = "Female"
        age = 21
    elif 11 == int(user):
        gender = "Female"
        age = 22
    elif 15 == int(user):
        gender = "Female"
        age = 23
    elif 16 == int(user):
        gender = "Female"
        age = 24
    elif 2 == int(user):
        gender = "Male"
        age = 27
    elif 3 == int(user):
        gender = "Male"
        age = 25
    elif 4 == int(user):
        gender = "Male"
        age = 19
    elif 5 == int(user):
        gender = "Male"
        age = 25
    elif 6 == int(user):
        gender = "Male"
        age = 25
    elif 7 == int(user):
        gender = "Male"
        age = 21
    elif 9 == int(user):
        gender = "Male"
        age = 27
    elif 12 == int(user):
        gender = "Male"
        age = 21
    elif 13 == int(user):
        gender = "Male"
        age = 23
    elif 14 == int(user):
        gender = "Male"
        age = 23
    elif 17 == int(user):
        gender = "Male"
        age = 23
    elif 18 == int(user):
        gender = "Male"
        age = 21
    elif 19 == int(user):
        gender = "Male"
        age = 25
    elif 20 == int(user):
        gender = "Male"
        age = 24

    return gender, age


def get_threshold_within(df, part, sense):
    group = df.groupby(df[2])
    group = group.get_group(part).reset_index().groupby(4)

    minimum = -10
    maximum = -20

    if sense in group.groups.keys():
        minimum = group[3].min()[sense]
        maximum = group[3].max()[sense]

    return minimum, maximum


def get_threshold(df, part, limit):
    group = df.groupby(df[2])
    group = group.get_group(part).reset_index().groupby(4)

    minimum = -10
    maximum = -20

    first = -1

    if 3 in group.groups.keys():
        maximum = group[3].max()[3]
    else:
        if 2 in group.groups.keys():
            maximum = group[3].max()[2]

    if 2 not in group.groups.keys():
        if 3 in group.groups.keys():
            minimum = group[3].min()[3]
    else:
        min_reversal = []
        for i in range(df.shape[0] - 1, -1, -1):
            row = df.iloc[i]
            if row[2] == part:
                sense = row[4]
                if sense == 2 or sense == 1:
                    if first == -1:
                        if sense == 2:
                            first = sense
                            min_reversal.append(row[3])
                        else:
                            first = sense

                    # print(f'first: {first}, sense: {sense}, i: {i}, limit: {limit}')
                    if sense == 1 and i > 0 and limit > 0:
                        prev = df.iloc[i - 1]
                        if prev[2] == part and prev[4] == 2:
                            min_reversal.append(prev[3])
                            limit = limit - 1
        if len(min_reversal) > 0:
            minimum = stats.mean(min_reversal)

    return minimum, maximum


reformat_23 = pd.DataFrame()
reformat_33 = pd.DataFrame()

for file_name in glob.glob(path):
    df = pd.read_csv(file_name, header=None)

    user = re.findall(r'[^\/]+(?=\.)', file_name)

    gender, age = user_demo_map(user[0])

    grouped = df.groupby(df[2])

    for part in range(1, 7):
        group = grouped.get_group(part)
        moisture = group[1].iloc[0]
        min_3, max_3 = get_threshold_within(df, part, 3)
        minimum, maximum = get_threshold(df, part, 3)
        if int(min_3) >= 0 and int(max_3) >= 0:
            temp = pd.DataFrame(
                {"user": [user[0]], "gender": [gender], "age": [age], "part": [part], "moisture": [moisture],
                 "level": [3], "minimum": [min_3], "maximum": [max_3], "range": [max_3 - min_3]})
            reformat_33 = reformat_33.append(temp, ignore_index=True)

        if int(minimum) >= 0 and int(maximum) >= 0:
            temp = pd.DataFrame(
                {"user": [user[0]], "gender": [gender], "age": [age], "part": [part], "moisture": [moisture],
                 "minimum": [minimum], "maximum": [maximum], "range": [max_3 - min_3]})
            reformat_23 = reformat_23.append(temp, ignore_index=True)

            print(f"user: {user[0]}, part: {part}, minimum: {minimum}")

print(reformat_23['minimum'].mean())

reformat_23.to_csv("/Users/jalapatip/Work/HaRVI/ElectroResults/Study/threshold_23.csv", index=False)
reformat_33.to_csv("/Users/jalapatip/Work/HaRVI/ElectroResults/Study/threshold_33.csv", index=False)
