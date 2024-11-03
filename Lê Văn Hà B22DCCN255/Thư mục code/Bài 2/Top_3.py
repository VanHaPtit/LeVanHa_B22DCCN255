import pandas as pd

df = pd.read_csv(r'D:\Lê Văn Hà B22DCCN255\Thư mục code\result.csv', header=2)


df.columns = df.columns.str.strip()


df.replace("N/a", 0, inplace=True)


player_column = 'Name'  

columns_to_check = ['Age', 'Matches Played', 'Starts', 'Min', 'non-Penalty Goals', 'Penalty Goals', 'Assists',
                     'Yellow Cards', 'Red Cards', 'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR', 'Gls', 'Ast', 'G+A',
                     'G-PK', 'G+A-PK', 'xG', 'xAG', 'xG+xAG', 'npxG', 'npxG + xAG', 'GA', 'GA90', 'SoTA', 'Saves', 
                     'Save%', 'W', 'D', 'L', 'CS', 'CS%', 'PKatt', 'PKA', 'PKsv', 'PKm', 'Save%', 'Gls', 'Sh', 'SoT',
                     'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'FK', 'PK', 'PKatt', 'xG', 'npxG', 'npxG/Sh',
                     'G-xG', 'np:G-xG', 'Cmp', 'Att', 'Cmp%', 'TotDist', 'PrgDist', 'Cmp', 'Att', 'Cmp%', 'Cmp', 'Att', 
                     'Cmp%', 'Cmp', 'Att', 'Cmp%', 'Ast', 'xAG', 'xA', 'A-xAG', 'KP', '1/3', 'PPA', 'CrsPA', 'PrgP',
                     'Live', 'Dead', 'FK', 'TB', 'Sw', 'Crs', 'TI', 'CK', 'In', 'Out', 'Str', 'Cmp', 'Off', 'Blocks',
                     'SCA', 'SCA90', 'PassLive', 'PassDead', 'TO', 'Sh', 'Fld', 'Def', 'GCA', 'GCA90', 'PassLive', 
                     'PassDead', 'TO', 'Sh', 'Fld', 'Def', 'Tkl', 'TklW', 'Def 3rd', 'Mid 3rd', 'Att 3rd', 'Tkl', 'Att',
                     'Tkl%', 'Lost', 'Blocks', 'Sh', 'Pass', 'Int', 'Tkl+Int', 'Clr', 'Err', 'Touches', 'Def Pen', 'Def 3rd', 
                     'Mid 3rd', 'Att 3rd', 'Att Pen', 'Live', 'Att', 'Succ', 'Succ%', 'Tkld', 'Tkld%', 'Carries', 'TotDist', 
                     'ProDist', 'ProgC', '1/3', 'CPA', 'Mis', 'Dis', 'ReC', 'PrgR', 'Starts', 'Mn/Start', 'Compl', 'Subs', 
                     'Mn/Sub', 'unSub', 'PPM', 'onG', 'onGA', 'onxG', 'onxGA', 'Fls', 'Fld', 'Off', 'Crs', 'OG', 'Recov',
                     'Won', 'Lost', 'Won%']


for column in columns_to_check:
    if column not in df.columns:
        print(f"Cột '{column}' không tồn tại trong DataFrame.")

top_3_highest = {}
top_3_lowest = {}

for column in columns_to_check:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0)  
        
        # Lấy top 3 cao nhất
        top_3_highest[column] = df.nlargest(3, column)[[player_column, column]]
        
        # Lấy top 3 thấp nhất
        top_3_lowest[column] = df.nsmallest(3, column)[[player_column, column]]

# In kết quả cho từng chỉ số
for column in top_3_highest:
    if column in top_3_highest:  
        print(f"\nTop 3 cầu thủ có điểm cao nhất ở {column}:")
        print(top_3_highest[column][player_column].to_string(index=False))  

        print(f"\nTop 3 cầu thủ có điểm thấp nhất ở {column}:")
        print(top_3_lowest[column][player_column].to_string(index=False))  
