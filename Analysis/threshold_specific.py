import glob
import re
import warnings

import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/All/*.txt"


def sequence_generator(n):
    return pd.Series(range(0, len(n)))


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


def get_threshold(df, part, sense):
    group = df.groupby(df[2])
    group = group.get_group(part).reset_index().groupby(4)

    minimum = -10
    maximum = -20

    if sense in group.groups.keys():
        minimum = group[3].min()[sense]
        maximum = group[3].max()[sense]

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
        minimum, maximum = get_threshold(df, part, 3)
        if int(minimum) >= 0 & int(maximum) >= 0:
            temp = pd.DataFrame(
                {"user": [user[0]], "gender": [gender], "age": [age], "part": [part], "moisture": [moisture],
                 "level": [3], "minimum": [minimum], "maximum": [maximum], "range": [maximum - minimum]})
            reformat = reformat.append(temp, ignore_index=True)
            print(f"user: {user[0]}, part: {part}, minimum: {minimum}")

reformat.to_csv("/Users/jalapatip/Work/HaRVI/ElectroResults/Study/threshold_specific.csv", index=False)
