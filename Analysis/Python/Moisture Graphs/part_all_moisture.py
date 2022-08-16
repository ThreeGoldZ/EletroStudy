import matplotlib.pylab as plt
import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/threshold_specific.csv"

n = 1

df = pd.read_csv(path)

part_group = df.groupby(['part'])

part = part_group.get_group(n)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)

for index, row in part.iterrows():
    plt.bar(row['moisture'], row['range'], bottom=row['minimum'], label=row['user'], alpha=0.5)


# for index, row in part.iterrows():
#     # print(row)
#     # row['moisture'] = row['moisture'].apply(str)
#     # plt.bar(row['moisture'], row['range'], bottom=row['minimum'], label=row['user'], alpha=0.6)
#     # plt.scatter(row['moisture'], row['minimum'], label=row['user'], alpha=0.6)
#     plt.scatter(row['moisture'], row['maximum'], label=row['user'], alpha=0.6)
#     # plt.scatter(row['moisture'], row['minimum'], label=row['user'])


plt.legend(bbox_to_anchor=(1, 1))
plt.suptitle(f'Moisture vs [Sensitivity and Endurance] for Part {n}', fontsize=20)
plt.show()
