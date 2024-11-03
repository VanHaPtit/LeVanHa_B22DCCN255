import pandas as pd


final_results = []


df = pd.read_csv(r'D:\Lê Văn Hà B22DCCN255\Thư mục code\result.csv', header=[0, 1, 2])

for col_index in range(4, df.shape[1]):
    column = df.iloc[:, col_index]
    column_numeric = pd.to_numeric(column, errors='coerce')  

    # Tính toán median, mean, và std cho toàn giải
    median_value_all = round(column_numeric.median(), 2)
    mean_value_all = round(column_numeric.mean(), 2)
    std_value_all = round(column_numeric.std(), 2)


    # Thêm kết quả cho toàn giải
    if col_index == 4:  # Nếu là attribute đầu tiên
        final_results.append(['All', median_value_all, mean_value_all, std_value_all])
    else:  # Các attribute khác
        final_results[0].extend([median_value_all, mean_value_all, std_value_all])



    # Tính toán cho từng đội
    for team_name, team_data in df.groupby(('Unnamed: 2_level_0', 'Unnamed: 2_level_1', 'Team')):
        team_column = pd.to_numeric(team_data.iloc[:, col_index], errors='coerce')  
        team_median = round(team_column.median(), 2)
        team_mean = round(team_column.mean(), 2)
        team_std = round(team_column.std(), 2)

        # Kiểm tra nếu đội đã có trong final_results
        found = False
        for row in final_results:
            if row[0] == team_name:
                # Cập nhật hàng của đội với các chỉ số mới
                row.extend([team_median, team_mean, team_std])
                found = True
                break

        if not found:
            # Nếu đội chưa có trong final_results, thêm mới
            final_results.append([team_name, team_median, team_mean, team_std])

final_df = pd.DataFrame(final_results)


column_titles = ['Team']
for col_index in range(4, df.shape[1]):
    column_titles.extend([f'Median of {df.columns[col_index][2]}',
                          f'Mean of {df.columns[col_index][2]}',
                          f'Std of {df.columns[col_index][2]}'])

final_df.columns = column_titles

# Ghi kết quả ra file results2.csv
print(final_df)
final_df.to_csv(r'D:\Lê Văn Hà B22DCCN255\Thư mục code\result2.csv', index=False)