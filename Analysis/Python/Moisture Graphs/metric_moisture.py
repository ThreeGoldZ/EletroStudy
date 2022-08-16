import matplotlib.pylab as plt
import pandas as pd

path = r"/Users/jalapatip/Work/HaRVI/ElectroResults/Study/threshold_specific.csv"

metric = 'maximum'


figure, axis = plt.subplots(3, 2)

df = pd.read_csv(path)

part_group = df.groupby(['part'])

# 1
part = part_group.get_group(1)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)
for index, row in part.iterrows():
    axis[0, 0].scatter(row['moisture'], row[metric], label=row['user'], alpha=0.6)
    axis[0, 0].set_title("Part 1")

# 4
part = part_group.get_group(4)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)
for index, row in part.iterrows():
    axis[0, 1].scatter(row['moisture'], row[metric], label=row['user'], alpha=0.6)
    axis[0, 1].set_title("Part 4")

# 2
part = part_group.get_group(2)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)
for index, row in part.iterrows():
    axis[1, 0].scatter(row['moisture'], row[metric], label=row['user'], alpha=0.6)
    axis[1, 0].set_title("Part 2")

# 5
part = part_group.get_group(5)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)
for index, row in part.iterrows():
    axis[1, 1].scatter(row['moisture'], row[metric], label=row['user'], alpha=0.6)
    axis[1, 1].set_title("Part 5")

# 3
part = part_group.get_group(3)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)
for index, row in part.iterrows():
    axis[2, 0].scatter(row['moisture'], row[metric], label=row['user'], alpha=0.6)
    axis[2, 0].set_title("Part 3")

# 6
part = part_group.get_group(6)
part = part.sort_values(by=['moisture'])
part['moisture'] = part['moisture'].apply(str)
for index, row in part.iterrows():
    axis[2, 1].scatter(row['moisture'], row[metric], label=row['user'], alpha=0.6)
    axis[2, 1].set_title("Part 6")


# axis[0, 0].legend(bbox_to_anchor=(1.14, 1.2))
# axis[0, 1].legend(bbox_to_anchor=(1.14, 1.2))
# axis[1, 0].legend(bbox_to_anchor=(1.14, 1.25))
# axis[1, 1].legend(bbox_to_anchor=(1.14, 1.25))
# axis[2, 1].legend(bbox_to_anchor=(1.14, 1.0))

# plt.legend()
figure.suptitle('Moisture vs Max_Threshold', fontsize=20)
plt.show()
