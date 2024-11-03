import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Đường dẫn tới tệp CSV
csv_file_path = r'D:\Lê Văn Hà B22DCCN255\Thư mục code\result2.csv'
# Đọc tệp CSV với header đa tầng
df = pd.read_csv(csv_file_path, header=[0, 1, 2])



# Lấy tên các chỉ số từ cột thứ 5 trở đi (index 4)
attributes = df.columns[4:]



# Tạo thư mục cho các biểu đồ nếu cần
output_folder = r'D:\Lê Văn Hà B22DCCN255\Thư mục hình vẽ'
os.makedirs(output_folder, exist_ok=True)




# Vẽ histogram cho mỗi chỉ số trong toàn giải



for attribute in attributes:
    plt.figure(figsize=(10, 6))
    
    data = pd.to_numeric(df[attribute], errors='coerce').dropna()
    
    # Vẽ histogram với đường phân phối KDE
    sns.histplot(data, kde=True, bins=20, color='skyblue')
    
    plt.title(f'Histogram of {attribute[2]} for All Players')
    plt.xlabel(attribute[2])
    plt.ylabel('Frequency')
    
    # Lưu biểu đồ vào thư mục
    output_path = os.path.join(output_folder, f'{attribute[2]}_All.png')
    print(f'Saving histogram for all players to: {output_path}')  
    plt.savefig(output_path)
    plt.close()


# Vẽ histogram cho mỗi chỉ số cho từng đội
if ('Unnamed: 2_level_0', 'Unnamed: 2_level_1', 'Team') in df.columns:
    for attribute in attributes:
        for team_name, team_data in df.groupby(('Unnamed: 2_level_0', 'Unnamed: 2_level_1', 'Team')):
            plt.figure(figsize=(10, 6))
            
            team_column = pd.to_numeric(team_data[attribute], errors='coerce').dropna()
            
            sns.histplot(team_column, kde=True, bins=20, color='orange')
            
            plt.title(f'Histogram of {attribute[2]} for Team {team_name}')
            plt.xlabel(attribute[2])
            plt.ylabel('Frequency')
            
            # Tạo thư mục cho đội nếu chưa tồn tại
            team_folder = os.path.join(output_folder, team_name)
            os.makedirs(team_folder, exist_ok=True)  # Tạo thư mục đội
            
            # Lưu biểu đồ vào thư mục
            team_output_path = os.path.join(team_folder, f'{attribute[2]}_{team_name}.png')
            
            # Kiểm tra xem có lưu thành công không
            try:
                plt.savefig(team_output_path)
                print(f'Saving histogram for team {team_name} to: {team_output_path}')  # In ra đường dẫn lưu
            except Exception as e:
                print(f'Không lưu thành công cho biểu đồ của đội {team_name}: {e}')  # Thông báo không thành công
            
            plt.close()
else:
    print('Không tìm thấy các cột nhóm cần thiết cho việc phân nhóm dữ liệu.')

# Thông báo hoàn tất
print("Biểu đồ đã được lưu vào thư mục:", output_folder)
