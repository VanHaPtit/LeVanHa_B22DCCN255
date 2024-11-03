

import csv
max_stats = {}



with open('D:\\Slide 28 tech\\BTL\\BTL\\bai1\\file\\squad_data.txt', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')



    for row in reader:
        for stat, value in row.items():
            try:

                value = float(value)

                if stat not in max_stats:
                    max_stats[stat] = (row['name'], value)
                else:

                    if value > max_stats[stat][1]:
                        max_stats[stat] = (row['name'], value)
            except ValueError:

                continue


for stat, (team, value) in max_stats.items():
    print(f"Đội bóng có {stat} cao nhất là {team} với giá trị {value}")




import pandas as pd
from collections import Counter



file_path = 'D:/Slide 28 tech/BTL/BTL/bai1/file/squad_data.txt'



try:
    df = pd.read_csv(file_path, delimiter='\t')
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

top_teams = []

top_teams.append(df.loc[df['Gls'].idxmax(), 'name'])
top_teams.append(df.loc[df['Ast'].idxmax(), 'name'])
top_teams.append(df.loc[df['SoT'].idxmax(), 'name'])
top_teams.append(df.loc[df['G/Sh'].idxmax(), 'name'])
top_teams.append(df.loc[df['G/SoT'].idxmax(), 'name'])

top_teams.append(df.loc[df['Poss'].idxmax(), 'name'])
top_teams.append(df.loc[df['Pass_Cmp'].idxmax(), 'name'])
top_teams.append(df.loc[df['Pass_Cmp%'].idxmax(), 'name'])

top_teams.append(df.loc[df['CS'].idxmax(), 'name'])
top_teams.append(df.loc[df['CS%'].idxmax(), 'name'])
top_teams.append(df.loc[df['Save%'].idxmax(), 'name'])
top_teams.append(df.loc[df['TklW'].idxmax(), 'name'])

top_teams.append(df.loc[df['W'].idxmax(), 'name'])
top_teams.append(df.loc[df['D'].idxmax(), 'name'])



team_counts = Counter(top_teams)



best_team = team_counts.most_common(1)[0]


print("Top team in each category:")
for team, count in team_counts.items():
    print(f"{team}: {count} categories")

print(f"\nThe team with the best overall performance is: {best_team[0]} with {best_team[1]} top categories")

